#!/usr/bin/env python3
"""Build Reef's intermediate 8x9 standard atlas from the approved GIF rows."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image


CELL_WIDTH = 192
CELL_HEIGHT = 208
COLUMNS = 8
ROWS = 9
ROW_SPECS = (
    ("idle", 6),
    ("running-right", 8),
    ("running-left", 8),
    ("waving", 4),
    ("jumping", 5),
    ("failed", 8),
    ("waiting", 6),
    ("running", 6),
    ("review", 6),
)


def normalize_transparency(image: Image.Image) -> Image.Image:
    rgba = image.convert("RGBA")
    data = bytearray(rgba.tobytes())
    for offset in range(0, len(data), 4):
        if data[offset + 3] == 0:
            data[offset : offset + 3] = b"\x00\x00\x00"
    return Image.frombytes("RGBA", rgba.size, bytes(data))


def load_gif_frames(path: Path, expected_count: int) -> list[Image.Image]:
    with Image.open(path) as gif:
        if gif.size != (CELL_WIDTH, CELL_HEIGHT):
            raise ValueError(
                f"{path.name}: expected {CELL_WIDTH}x{CELL_HEIGHT}, got {gif.width}x{gif.height}"
            )
        if gif.n_frames != expected_count:
            raise ValueError(
                f"{path.name}: expected {expected_count} frames, got {gif.n_frames}"
            )
        frames = []
        for index in range(gif.n_frames):
            gif.seek(index)
            frame = normalize_transparency(gif.copy())
            if frame.getchannel("A").getbbox() is None:
                raise ValueError(f"{path.name}: frame {index} is empty")
            frames.append(frame)
        return frames


def build(source_dir: Path, output_dir: Path) -> dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    atlas = Image.new(
        "RGBA",
        (COLUMNS * CELL_WIDTH, ROWS * CELL_HEIGHT),
        (0, 0, 0, 0),
    )
    row_report = []

    for row, (state, frame_count) in enumerate(ROW_SPECS):
        source = source_dir / f"{state}.gif"
        frames = load_gif_frames(source, frame_count)
        for column, frame in enumerate(frames):
            atlas.alpha_composite(frame, (column * CELL_WIDTH, row * CELL_HEIGHT))
        row_report.append(
            {"row": row, "state": state, "frames": frame_count, "source": source.name}
        )

    atlas = normalize_transparency(atlas)
    png_path = output_dir / "spritesheet.png"
    webp_path = output_dir / "spritesheet.webp"
    atlas.save(png_path)
    atlas.save(webp_path, format="WEBP", lossless=True, quality=100, method=6, exact=True)

    report = {
        "ok": True,
        "kind": "intermediate-standard-atlas",
        "publishable": False,
        "width": atlas.width,
        "height": atlas.height,
        "cellWidth": CELL_WIDTH,
        "cellHeight": CELL_HEIGHT,
        "rows": row_report,
        "spritesheetPng": png_path.name,
        "spritesheetWebp": webp_path.name,
    }
    (output_dir / "build.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=Path("docs/assets/animations"),
        help="Directory containing the nine approved row GIFs.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("build/reef-standard"),
        help="Directory for the intermediate spritesheet and build report.",
    )
    args = parser.parse_args()
    report = build(args.source_dir.resolve(), args.output_dir.resolve())
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
