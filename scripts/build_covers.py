"""Build the Featured Software cover images from each project's real screenshots.

Run manually whenever a project's screenshots change:

    python scripts/build_covers.py

The script reads scripts/projects.json, downloads the screenshots listed under
"cover" from each repository's default branch, and frames them on a uniform
navy canvas so every Featured card has the same size and visual weight.
Output: assets/projects/<no>-<slug>.png

Requires Pillow. Nothing here runs in CI; the generated images are committed.
"""

from __future__ import annotations

import io
import json
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "scripts" / "projects.json"
OUT_DIR = ROOT / "assets" / "projects"

W, H = 1200, 750
BOTTOM_GAP = 48  # transparent strip below the card; spaces text from the image when it stacks on mobile
CANVAS_RADIUS = 28
SHOT_RADIUS = 14
BOX = (72, 92, W - 72, H - 60)  # area the screenshots are fitted into
GAP = 40

BG_TOP = (16, 24, 46)
BG_BOTTOM = (11, 16, 32)
GRID = (38, 52, 81)
BORDER = (38, 52, 81)
SHOT_BORDER = (52, 70, 108)
MUTED = (110, 127, 160)

FONT_CANDIDATES = {
    "mono_bold": [
        "C:/Windows/Fonts/consolab.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
        "/System/Library/Fonts/Menlo.ttc",
    ],
    "mono": [
        "C:/Windows/Fonts/consola.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/System/Library/Fonts/Menlo.ttc",
    ],
}


def hex_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def load_font(kind: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in FONT_CANDIDATES[kind]:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


def fetch_image(owner: str, repo: str, branch: str, path: str) -> Image.Image:
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    request = urllib.request.Request(url, headers={"User-Agent": "deuxdoom-profile-covers"})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
    return Image.open(io.BytesIO(data)).convert("RGBA")


def rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius, fill=255)
    return mask


def background(accent: tuple[int, int, int]) -> Image.Image:
    canvas = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(canvas)
    for y in range(H):
        t = y / (H - 1)
        color = tuple(round(BG_TOP[i] + (BG_BOTTOM[i] - BG_TOP[i]) * t) for i in range(3))
        draw.line([(0, y), (W, y)], fill=color + (255,))

    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    grid_draw = ImageDraw.Draw(grid)
    for x in range(0, W, 40):
        grid_draw.line([(x, 0), (x, H)], fill=GRID + (70,))
    for y in range(0, H, 40):
        grid_draw.line([(0, y), (W, y)], fill=GRID + (70,))
    fade = Image.new("L", (W, H))
    fade_draw = ImageDraw.Draw(fade)
    for y in range(H):
        fade_draw.line([(0, y), (W, y)], fill=round(255 * (1 - y / H) ** 1.6))
    grid.putalpha(Image.composite(grid.getchannel("A"), Image.new("L", (W, H), 0), fade))
    canvas = Image.alpha_composite(canvas, grid)

    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse((W * 0.18, H * 0.3, W * 0.82, H * 1.05), fill=accent + (64,))
    glow = glow.filter(ImageFilter.GaussianBlur(110))
    return Image.alpha_composite(canvas, glow)


def fit(image: Image.Image, max_w: int, max_h: int) -> Image.Image:
    scale = min(max_w / image.width, max_h / image.height)
    size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
    return image.resize(size, Image.LANCZOS)


def layout(shots: list[Image.Image]) -> list[tuple[Image.Image, tuple[int, int]]]:
    box_w, box_h = BOX[2] - BOX[0], BOX[3] - BOX[1]
    if len(shots) == 1:
        placed = [fit(shots[0], box_w, box_h)]
    else:
        primary = fit(shots[0], int(box_w * 0.55), box_h)
        rest_w = (box_w - primary.width - GAP * (len(shots) - 1)) // (len(shots) - 1)
        placed = [primary] + [fit(s, rest_w, box_h) for s in shots[1:]]

    total_w = sum(p.width for p in placed) + GAP * (len(placed) - 1)
    x = BOX[0] + (box_w - total_w) // 2
    result = []
    for p in placed:
        y = BOX[1] + (box_h - p.height) // 2
        result.append((p, (x, y)))
        x += p.width + GAP
    return result


def paste_shot(canvas: Image.Image, shot: Image.Image, pos: tuple[int, int]) -> Image.Image:
    x, y = pos
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle(
        (x, y + 18, x + shot.width, y + shot.height + 18), SHOT_RADIUS, fill=(0, 0, 0, 150)
    )
    canvas = Image.alpha_composite(canvas, shadow.filter(ImageFilter.GaussianBlur(26)))

    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    layer.paste(shot, (x, y), rounded_mask(shot.size, SHOT_RADIUS))
    canvas = Image.alpha_composite(canvas, layer)
    ImageDraw.Draw(canvas).rounded_rectangle(
        (x, y, x + shot.width - 1, y + shot.height - 1), SHOT_RADIUS, outline=SHOT_BORDER + (255,), width=2
    )
    return canvas


def label(canvas: Image.Image, project: dict, total: int, accent: tuple[int, int, int]) -> None:
    draw = ImageDraw.Draw(canvas)
    number_font = load_font("mono_bold", 34)
    small_font = load_font("mono", 22)
    draw.text((44, 34), project["no"], font=number_font, fill=accent)
    number_w = draw.textlength(project["no"], font=number_font)
    draw.text((44 + number_w + 12, 44), f"/ {total:02d}", font=small_font, fill=MUTED)
    name = project["name"].upper()
    name_w = draw.textlength(name, font=small_font)
    draw.text((W - 44 - name_w, 44), name, font=small_font, fill=MUTED)
    draw.rounded_rectangle((44, H - 34, 44 + 120, H - 30), 2, fill=accent)


def build(project: dict, owner: str, branch: str, total: int) -> Path:
    accent = hex_rgb(project["accent"])
    shots = [fetch_image(owner, project["repo"], branch, path) for path in project["cover"]]
    canvas = background(accent)
    for shot, pos in layout(shots):
        canvas = paste_shot(canvas, shot, pos)
    label(canvas, project, total, accent)

    ImageDraw.Draw(canvas).rounded_rectangle(
        (0, 0, W - 1, H - 1), CANVAS_RADIUS, outline=BORDER + (255,), width=2
    )
    canvas.putalpha(Image.composite(canvas.getchannel("A"), Image.new("L", canvas.size, 0), rounded_mask(canvas.size, CANVAS_RADIUS)))

    framed = Image.new("RGBA", (W, H + BOTTOM_GAP), (0, 0, 0, 0))
    framed.paste(canvas, (0, 0))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{project['no']}-{project['slug']}.png"
    framed.save(out, optimize=True)
    return out


def main() -> int:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    projects = config["projects"]
    for project in projects:
        out = build(project, config["owner"], config["branch"], len(projects))
        print(f"{out.relative_to(ROOT)}  {out.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
