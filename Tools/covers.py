#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates the 1200×630 social covers for every article, in the dark
liquid-glass style.

Titles and tags are read from content/posts/*.py, so covers never drift from
the articles. Fonts live in _src/fonts/ (Archivo Black + Space Mono, SIL OFL).

Run:  python3 make_covers.py
"""
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import config as cfg
from core.pages import load_posts

ROOT = cfg.ROOT

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
TITLE_FONT = os.path.join(FONT_DIR, "ArchivoBlack-Regular.ttf")
MONO_FONT = os.path.join(FONT_DIR, "SpaceMono-Bold.ttf")

INK = (11, 11, 9)
INK_2 = (23, 23, 15)
PAPER = (242, 240, 232)
MUTED = (150, 148, 140)
YELLOW = (232, 255, 46)
BLUE = (47, 46, 240)
RED = (232, 67, 44)

ACCENT = {
    "Leadership": BLUE,
    "Case Study": RED,
    "Startups": YELLOW,
    "Consulting": BLUE,
    "Automation & AI": YELLOW,
    "Web Development": RED,
    "Pricing": YELLOW,
    "Project Management": BLUE,
}

W, H = 1200, 630


def short_title(h1):
    """The punchy half of the headline — everything before the first : ( or ?"""
    m = re.split(r"[:(]", h1, maxsplit=1)[0]
    if "?" in h1 and len(m) > len(h1.split("?")[0]):
        m = h1.split("?")[0] + "?"
    return m.strip().rstrip(",").upper()


def blob(size, colour, alpha):
    """A soft radial glow, the same one the site uses behind the glass."""
    layer = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(layer)
    steps = 60
    for i in range(steps, 0, -1):
        r = int(size / 2 * i / steps)
        a = int(alpha * (1 - i / steps) ** 2)
        d.ellipse([size // 2 - r, size // 2 - r, size // 2 + r, size // 2 + r], fill=a)
    tint = Image.new("RGB", (size, size), colour)
    return tint, layer


def wrap(draw, text, font, max_w):
    lines, line = [], ""
    for word in text.split():
        probe = (line + " " + word).strip()
        if draw.textlength(probe, font=font) <= max_w:
            line = probe
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def build_cover(slug, tag, title):
    accent = ACCENT.get(tag, BLUE)

    # base: vertical gradient from #17170f to #0b0b09
    img = Image.new("RGB", (W, H), INK)
    grad = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        grad.line([(0, y), (W, y)],
                  fill=tuple(int(INK_2[i] + (INK[i] - INK_2[i]) * t) for i in range(3)))

    # two colour glows, as on the site
    for colour, alpha, pos, size in (
        (accent, 150, (-120, -180), 760),
        (BLUE if accent is not BLUE else RED, 80, (W - 460, H - 300), 640),
    ):
        tint, mask = blob(size, colour, alpha)
        img.paste(tint, pos, mask)

    d = ImageDraw.Draw(img, "RGBA")

    # thin inner hairline — the edge of the glass
    d.rounded_rectangle([18, 18, W - 19, H - 19], radius=26,
                        outline=(255, 255, 255, 38), width=2)

    # tag chip
    mono = ImageFont.truetype(MONO_FONT, 21)
    label = tag.upper()
    tw = d.textlength(label, font=mono)
    d.rounded_rectangle([66, 74, 66 + tw + 40, 74 + 42], radius=21,
                        fill=accent + (235,), outline=(255, 255, 255, 90), width=1)
    chip_ink = INK if accent is not BLUE else PAPER
    d.text((86, 84), label, font=mono, fill=chip_ink)

    # title, shrunk until it fits in three lines
    size = 78
    while size > 38:
        f = ImageFont.truetype(TITLE_FONT, size)
        lines = wrap(d, title, f, W - 150)
        if len(lines) <= 3:
            break
        size -= 4
    f = ImageFont.truetype(TITLE_FONT, size)
    lines = wrap(d, title, f, W - 150)
    lh = int(size * 1.2)
    y = 210 + (3 - len(lines)) * lh // 2
    for line in lines:
        d.text((68, y), line, font=f, fill=PAPER)
        y += lh

    # footer
    small = ImageFont.truetype(MONO_FONT, 19)
    d.rounded_rectangle([68, 530, 138, 548], radius=9, fill=accent + (235,))
    d.text((156, 528), "GANZA CONSULTING — BLOG", font=small, fill=MUTED)

    out = os.path.join(ROOT, "assets", "img", "blog", f"{slug}-cover.png")
    img.save(out, optimize=True)
    return out, size, len(lines)


def build_thumbs(width=760):
    """Small WebP copies for the blog index — the 1200px PNGs are for social
    cards only, shipping 12 of them to a listing page costs ~450 KB."""
    saved = 0
    for f in sorted(os.listdir(os.path.join(ROOT, "assets", "img", "blog"))):
        if not f.endswith("-cover.png"):
            continue
        src = os.path.join(ROOT, "assets", "img", "blog", f)
        dst = src.replace("-cover.png", "-card.webp")
        im = Image.open(src)
        im = im.resize((width, round(width * im.height / im.width)), Image.LANCZOS)
        im.save(dst, "WEBP", quality=82, method=6)
        saved += os.path.getsize(src) - os.path.getsize(dst)
    print(f"thumbnails written, {saved // 1024} KB saved across the listing")


def main():
    if not os.path.exists(TITLE_FONT):
        raise SystemExit(f"missing fonts in {FONT_DIR} — see README")
    for post in load_posts():
        title = short_title(post["h1"]["en"])
        _, size, lines = build_cover(post["slug"], post["tag"]["en"], title)
        print(f"{post['slug']:<44} {size:>3}px / {lines} lines — {title[:44]}")
    build_thumbs()


if __name__ == "__main__":
    main()
