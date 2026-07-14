#!/usr/bin/env python3
"""Build square, high-resolution, upload-ready animated GIFs."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageSequence


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "docs" / "assets" / "animations"
ATLAS_PATH = ROOT / "dist" / "reef" / "spritesheet.webp"
OUTPUT_DIR = ROOT / "docs" / "assets" / "upload-ready-512"
CANVAS_SIZE = 512
SUBJECT_HEIGHT = 464
MAX_BYTES = 1_000_000
CELL_WIDTH = 192
CELL_HEIGHT = 208
ROW_SPECS = (
    ("idle", 0, 6),
    ("running-right", 1, 8),
    ("running-left", 2, 8),
    ("waving", 3, 4),
    ("jumping", 4, 5),
    ("failed", 5, 8),
    ("waiting", 6, 6),
    ("running", 7, 6),
    ("review", 8, 6),
)


def complete_cycle(frames: list[Image.Image], durations: list[int]) -> tuple[list[Image.Image], list[int]]:
    """Add a readable endpoint hold and a return-to-start phase."""
    if len(frames) < 2:
        return frames, durations

    # Forward action, then the interior poses in reverse and an explicit return
    # to the starting pose. A longer endpoint duration provides the visual hold.
    indices = list(range(len(frames))) + list(range(len(frames) - 2, 0, -1)) + [0]
    cycle_frames = [frames[index].copy() for index in indices]
    cycle_durations = [durations[index] for index in indices]
    cycle_durations[len(frames) - 1] = max(cycle_durations[len(frames) - 1], 180)
    cycle_durations[-1] = max(cycle_durations[-1], 180)
    return cycle_frames, cycle_durations


def prepare_frame(frame: Image.Image) -> Image.Image:
    rgba = frame.convert("RGBA")
    bbox = rgba.getbbox()
    if bbox:
        rgba = rgba.crop(bbox)

    scale = min((CANVAS_SIZE - 24) / rgba.width, SUBJECT_HEIGHT / rgba.height)
    size = (max(1, round(rgba.width * scale)), max(1, round(rgba.height * scale)))
    # Resize in premultiplied-alpha space so the RGB values hidden behind
    # transparent chroma-key pixels cannot bleed back into visible edges.
    rgba = rgba.convert("RGBa").resize(size, Image.Resampling.LANCZOS).convert("RGBA")
    rgba = ImageEnhance.Sharpness(rgba).enhance(1.12)

    canvas = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    x = (CANVAS_SIZE - rgba.width) // 2
    y = CANVAS_SIZE - 20 - rgba.height
    canvas.alpha_composite(rgba, (x, y))
    return canvas


def save_under_limit(frames: list[Image.Image], durations: list[int], output: Path) -> int:
    for colors in (128, 96, 64, 48, 32):
        paletted = []
        for frame in frames:
            alpha = frame.getchannel("A")
            # GIF transparency is binary. Quantize the sprite's straight RGB
            # values directly instead of first matting antialiased pixels
            # against magenta, which would bake a purple fringe into every
            # edge that crosses the alpha threshold below.
            rgb = frame.convert("RGB")
            quantized = rgb.quantize(colors=colors - 1, method=Image.Quantize.MEDIANCUT)

            # Reserve palette index 255 for transparency.
            palette = quantized.getpalette()[: (colors - 1) * 3]
            palette.extend([0] * (255 * 3 - len(palette)))
            palette.extend([255, 0, 255])
            quantized.putpalette(palette)
            transparent = Image.new("P", frame.size, 255)
            transparent.putpalette(palette)
            transparent.paste(quantized, mask=alpha.point(lambda value: 255 if value >= 32 else 0))
            paletted.append(transparent)

        paletted[0].save(
            output,
            save_all=True,
            append_images=paletted[1:],
            duration=durations,
            loop=0,
            disposal=2,
            transparency=255,
            optimize=True,
        )
        size = output.stat().st_size
        if size <= MAX_BYTES:
            return colors
    raise RuntimeError(f"Could not compress {output.name} below {MAX_BYTES} bytes")


def load_durations(path: Path, expected_count: int) -> list[int]:
    with Image.open(path) as source:
        if source.n_frames != expected_count:
            raise ValueError(
                f"{path.name}: expected {expected_count} frames, got {source.n_frames}"
            )
        durations = []
        for frame in ImageSequence.Iterator(source):
            durations.append(int(frame.info.get("duration", source.info.get("duration", 120))))
    return durations


def load_atlas_frames(atlas: Image.Image, row: int, frame_count: int) -> list[Image.Image]:
    frames = []
    for column in range(frame_count):
        left = column * CELL_WIDTH
        top = row * CELL_HEIGHT
        frame = atlas.crop((left, top, left + CELL_WIDTH, top + CELL_HEIGHT))
        if frame.getchannel("A").getbbox() is None:
            raise ValueError(f"atlas row {row}, frame {column} is empty")
        frames.append(prepare_frame(frame))
    return frames


def make_contact_sheet(first_frames: list[tuple[str, Image.Image]]) -> None:
    cell = 320
    sheet = Image.new("RGB", (cell * 3, cell * 3), (16, 24, 38))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default(size=20)
    for index, (name, frame) in enumerate(first_frames):
        thumb = frame.copy()
        thumb.thumbnail((260, 260), Image.Resampling.LANCZOS)
        x = (index % 3) * cell + (cell - thumb.width) // 2
        y = (index // 3) * cell + 12
        sheet.paste(thumb, (x, y), thumb)
        label_box = draw.textbbox((0, 0), name, font=font)
        label_width = label_box[2] - label_box[0]
        draw.text(((index % 3) * cell + (cell - label_width) // 2, y + 268), name, fill=(235, 244, 255), font=font)
    sheet.save(OUTPUT_DIR / "contact-sheet.png", optimize=True)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = []
    first_frames = []

    with Image.open(ATLAS_PATH) as atlas_source:
        atlas = atlas_source.convert("RGBA")
        expected_size = (CELL_WIDTH * 8, CELL_HEIGHT * 11)
        if atlas.size != expected_size:
            raise ValueError(f"expected v2 atlas {expected_size}, got {atlas.size}")

        for state, row, frame_count in sorted(ROW_SPECS, key=lambda item: f"{item[0]}.gif"):
            source = SOURCE_DIR / f"{state}.gif"
            durations = load_durations(source, frame_count)
            frames = load_atlas_frames(atlas, row, frame_count)
            frames, durations = complete_cycle(frames, durations)
            output = OUTPUT_DIR / source.name
            colors = save_under_limit(frames, durations, output)
            with Image.open(output) as encoded:
                encoded_frame_count = encoded.n_frames
            first_frames.append((state, frames[0]))
            manifest.append(
                {
                    "file": output.name,
                    "resolution": [CANVAS_SIZE, CANVAS_SIZE],
                    "frames": encoded_frame_count,
                    "duration_ms": sum(durations),
                    "size_bytes": output.stat().st_size,
                    "palette_colors": colors,
                    "loop": "infinite",
                }
            )

    make_contact_sheet(first_frames)
    (OUTPUT_DIR / "manifest.json").write_text(
        json.dumps(
            {
                "requirements": {"max_bytes": MAX_BYTES, "max_frames": 60},
                "assets": manifest,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    for item in manifest:
        print(
            f"{item['file']}: {item['resolution'][0]}x{item['resolution'][1]}, "
            f"{item['frames']} frames, {item['size_bytes']} bytes"
        )


if __name__ == "__main__":
    main()
