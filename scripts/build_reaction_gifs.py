#!/usr/bin/env python3
"""Build 512px looping GIFs from 2x2 reaction sprite sheets."""

from __future__ import annotations

import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "reaction-run" / "spritesheets"
OUTPUT_DIR = ROOT / "docs" / "assets" / "reactions-512"
ARCHIVE_PATH = OUTPUT_DIR / "reef-reactions-512.zip"
CANVAS_SIZE = 512
MAX_BYTES = 1_000_000

REACTIONS = {
    "01-licking": {"label": "舔舔舔", "durations": [180, 150, 180, 150]},
    "02-glow-sticks": {"label": "揮螢光棒", "durations": [160, 140, 180, 140]},
    "03-startled-shake": {"label": "驚嚇到上下震動", "durations": [130, 90, 110, 90]},
    "04-blush-cover": {"label": "臉紅遮臉 不行不行", "durations": [190, 170, 150, 170]},
    "05-smoke-puff": {"label": "吐一口菸", "durations": [220, 170, 230, 240]},
    "06-rainbow": {"label": "吐彩虹", "durations": [190, 150, 230, 150]},
    "07-tail-wag": {"label": "開心的搖尾巴", "durations": [130, 110, 130, 110]},
    "08-ugly-cry": {"label": "醜哭", "durations": [210, 170, 230, 170]},
    "09-flirty-drool": {"label": "色色吐舌頭＋流口水", "durations": [200, 150, 210, 150]},
    "10-terror-scream": {"label": "阿~~~~（驚恐叫）", "durations": [170, 140, 220, 150]},
}

# Frame-specific registration corrections measured from the shark's hat, torso,
# and shorts rather than from the full silhouette. This keeps expressive props
# (glow sticks, rainbow, tears, motion marks, and the wagging tail) free to move
# while preventing the captain's body from drifting between generated panels.
STABILIZATION = {
    "01-licking": {
        "scale": 1.0,
        "offsets": [(-7, 0), (8, 0), (-7, 0), (7, 0)],
    },
    "02-glow-sticks": {
        "scale": 0.94,
        "offsets": [(-21, 2), (41, 3), (-12, 29), (20, 26)],
    },
    "03-startled-shake": {
        "scale": 0.90,
        "offsets": [(-8, 0), (45, 63), (-2, 55), (46, 88)],
    },
    "04-blush-cover": {
        "scale": 0.98,
        "offsets": [(-16, -2), (8, 1), (-4, 12), (11, 7)],
    },
    "05-smoke-puff": {
        "scale": 1.0,
        "offsets": [(-7, -2), (8, -4), (-6, 8), (6, 4)],
    },
    "06-rainbow": {
        "scale": 0.96,
        "offsets": [(-6, 0), (13, -5), (-24, 5), (13, 10)],
    },
    "07-tail-wag": {
        "scale": 1.0,
        "offsets": [(-12, -1), (7, -3), (-7, 3), (8, 2)],
    },
    "08-ugly-cry": {
        "scale": 0.97,
        "offsets": [(-15, 0), (6, 4), (-6, 15), (19, 15)],
    },
    "09-flirty-drool": {
        "scale": 1.0,
        "offsets": [(0, -1), (1, -3), (-2, -3), (1, -1)],
    },
    "10-terror-scream": {
        "scale": 0.97,
        "offsets": [(-6, 0), (5, -10), (-7, 19), (8, 6)],
    },
}

# A few large effects crossed the 2x2 panel boundary in the generated sheet.
# These rectangles remove only the detached spillover from the neighboring
# panel before registration; the character and intended effect remain intact.
FRAME_CLEANUP = {
    "02-glow-sticks": {3: [(0, 0, 45, 130)]},
    "06-rainbow": {3: [(0, 0, 40, CANVAS_SIZE)]},
}


def split_sheet(path: Path) -> list[Image.Image]:
    """Split an even 2x2 sprite sheet and normalize each frame."""
    with Image.open(path) as source:
        rgb = source.convert("RGB")
    if rgb.width % 2 or rgb.height % 2:
        raise ValueError(f"Sprite sheet must have even dimensions: {path}")

    half_width = rgb.width // 2
    half_height = rgb.height // 2
    boxes = (
        (0, 0, half_width, half_height),
        (half_width, 0, rgb.width, half_height),
        (0, half_height, half_width, rgb.height),
        (half_width, half_height, rgb.width, rgb.height),
    )
    return [
        rgb.crop(box).resize((CANVAS_SIZE, CANVAS_SIZE), Image.Resampling.LANCZOS)
        for box in boxes
    ]


def stabilize_frame(
    frame: Image.Image, scale: float, offset: tuple[int, int]
) -> Image.Image:
    """Apply a fixed scale and translation on a white 512px canvas."""
    if scale != 1.0:
        size = (round(CANVAS_SIZE * scale), round(CANVAS_SIZE * scale))
        frame = frame.resize(size, Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
    x = (CANVAS_SIZE - frame.width) // 2 + offset[0]
    y = (CANVAS_SIZE - frame.height) // 2 + offset[1]
    canvas.paste(frame, (x, y))
    return canvas


def stabilize_frames(stem: str, frames: list[Image.Image]) -> list[Image.Image]:
    registration = STABILIZATION[stem]
    for frame_index, boxes in FRAME_CLEANUP.get(stem, {}).items():
        draw = ImageDraw.Draw(frames[frame_index])
        for box in boxes:
            draw.rectangle(box, fill="white")
    return [
        stabilize_frame(frame, registration["scale"], offset)
        for frame, offset in zip(frames, registration["offsets"], strict=True)
    ]


def save_under_limit(
    frames: list[Image.Image], durations: list[int], output: Path
) -> int:
    """Save a looping GIF and reduce its palette until it is below 1 MB."""
    for colors in (128, 96, 64, 48, 40, 32, 24, 16):
        paletted = [
            frame.quantize(
                colors=colors,
                method=Image.Quantize.MEDIANCUT,
                dither=Image.Dither.FLOYDSTEINBERG,
            )
            for frame in frames
        ]
        paletted[0].save(
            output,
            save_all=True,
            append_images=paletted[1:],
            duration=durations,
            loop=0,
            disposal=2,
            optimize=True,
        )
        if output.stat().st_size <= MAX_BYTES:
            return colors
    raise RuntimeError(f"Could not compress {output.name} below {MAX_BYTES} bytes")


def make_contact_sheet(first_frames: list[tuple[str, Image.Image]]) -> None:
    cell = 300
    columns = 5
    rows = 2
    sheet = Image.new("RGB", (cell * columns, cell * rows), (17, 25, 39))
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default(size=18)
    for index, (name, frame) in enumerate(first_frames):
        thumbnail = frame.copy()
        thumbnail.thumbnail((260, 260), Image.Resampling.LANCZOS)
        column = index % columns
        row = index // columns
        x = column * cell + (cell - thumbnail.width) // 2
        y = row * cell + 4
        sheet.paste(thumbnail, (x, y))
        label = name.removeprefix("0").replace("-", " ")
        bounds = draw.textbbox((0, 0), label, font=font)
        label_width = bounds[2] - bounds[0]
        draw.text(
            (column * cell + (cell - label_width) // 2, row * cell + 270),
            label,
            fill=(235, 244, 255),
            font=font,
        )
    sheet.save(OUTPUT_DIR / "contact-sheet.png", optimize=True)


def make_all_frames_sheet(frame_rows: list[tuple[str, list[Image.Image]]]) -> None:
    """Create a visual QA sheet showing every animation keyframe."""
    label_width = 190
    cell = 200
    sheet = Image.new(
        "RGB",
        (label_width + cell * 4, cell * len(frame_rows)),
        (17, 25, 39),
    )
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default(size=18)

    for row, (name, frames) in enumerate(frame_rows):
        label = name.removeprefix("0").replace("-", " ")
        draw.multiline_text(
            (12, row * cell + 76),
            label,
            fill=(235, 244, 255),
            font=font,
            spacing=5,
        )
        for column, frame in enumerate(frames):
            thumbnail = frame.copy()
            thumbnail.thumbnail((190, 190), Image.Resampling.LANCZOS)
            x = label_width + column * cell + (cell - thumbnail.width) // 2
            y = row * cell + (cell - thumbnail.height) // 2
            sheet.paste(thumbnail, (x, y))

    sheet.save(OUTPUT_DIR / "all-frames-contact-sheet.png", optimize=True)


def make_archive(asset_names: list[str]) -> None:
    """Create a deterministic download archive from the generated assets."""
    with ZipFile(ARCHIVE_PATH, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name in [*asset_names, "manifest.json", "index.html"]:
            source = OUTPUT_DIR / name
            if not source.exists():
                raise FileNotFoundError(source)
            info = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, source.read_bytes(), compresslevel=9)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = []
    first_frames = []
    frame_rows = []

    for stem, metadata in REACTIONS.items():
        source = SOURCE_DIR / f"{stem}.png"
        if not source.exists():
            raise FileNotFoundError(source)
        frames = stabilize_frames(stem, split_sheet(source))
        durations = metadata["durations"]
        output = OUTPUT_DIR / f"{stem}.gif"
        colors = save_under_limit(frames, durations, output)

        with Image.open(output) as encoded:
            resolution = list(encoded.size)
            frame_count = encoded.n_frames
            loop = encoded.info.get("loop")

        item = {
            "file": output.name,
            "label": metadata["label"],
            "resolution": resolution,
            "frames": frame_count,
            "duration_ms": sum(durations),
            "size_bytes": output.stat().st_size,
            "palette_colors": colors,
            "loop": "infinite" if loop == 0 else loop,
            "source_sprite_sheet": str(source.relative_to(ROOT)),
        }
        manifest.append(item)
        first_frames.append((stem, frames[0]))
        frame_rows.append((stem, frames))
        print(
            f"{output.name}: {resolution[0]}x{resolution[1]}, "
            f"{frame_count} frames, {item['size_bytes']} bytes, {colors} colors"
        )

    make_contact_sheet(first_frames)
    make_all_frames_sheet(frame_rows)
    (OUTPUT_DIR / "manifest.json").write_text(
        json.dumps(
            {
                "requirements": {
                    "resolution": [CANVAS_SIZE, CANVAS_SIZE],
                    "max_bytes": MAX_BYTES,
                    "loop": "infinite",
                },
                "assets": manifest,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    make_archive([item["file"] for item in manifest])
    print(f"{ARCHIVE_PATH.name}: {ARCHIVE_PATH.stat().st_size} bytes")


if __name__ == "__main__":
    main()
