#!/usr/bin/env python3
"""Build square, high-resolution, upload-ready animated GIFs."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageSequence


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "docs" / "assets" / "animations"
OUTPUT_DIR = ROOT / "docs" / "assets" / "upload-ready-512"
CANVAS_SIZE = 512
SUBJECT_HEIGHT = 464
MAX_BYTES = 1_000_000


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
    # The source GIFs contain fully opaque chroma-key speckles around the
    # silhouette. Remove only strongly green pixels before scaling so those
    # artifacts are not enlarged by resampling.
    cleaned = []
    pixels = rgba.get_flattened_data() if hasattr(rgba, "get_flattened_data") else rgba.getdata()
    for red, green, blue, alpha in pixels:
        is_key_green = green > 110 and green > red * 1.2 and green > blue * 1.12
        cleaned.append((red, green, blue, 0 if is_key_green else alpha))
    rgba.putdata(cleaned)
    bbox = rgba.getbbox()
    if bbox:
        rgba = rgba.crop(bbox)

    scale = min((CANVAS_SIZE - 24) / rgba.width, SUBJECT_HEIGHT / rgba.height)
    size = (max(1, round(rgba.width * scale)), max(1, round(rgba.height * scale)))
    rgba = rgba.resize(size, Image.Resampling.LANCZOS)
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
            rgb = Image.new("RGB", frame.size, (255, 0, 255))
            rgb.paste(frame.convert("RGB"), mask=alpha)
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


def load_gif(path: Path) -> tuple[list[Image.Image], list[int]]:
    with Image.open(path) as source:
        frames = []
        durations = []
        for frame in ImageSequence.Iterator(source):
            frames.append(prepare_frame(frame))
            durations.append(int(frame.info.get("duration", source.info.get("duration", 120))))
    return frames, durations


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

    for source in sorted(SOURCE_DIR.glob("*.gif")):
        frames, durations = load_gif(source)
        frames, durations = complete_cycle(frames, durations)
        output = OUTPUT_DIR / source.name
        colors = save_under_limit(frames, durations, output)
        with Image.open(output) as encoded:
            encoded_frame_count = encoded.n_frames
        first_frames.append((source.stem, frames[0]))
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
