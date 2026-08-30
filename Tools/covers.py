#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Обложки 1200×630 для соцсетей — по одной на язык для каждой статьи,
плюс общая карточка сайта.

Заголовки и теги читаются из content/posts/*.py, поэтому обложки не могут
разойтись со статьями. Шрифты лежат в Tools/fonts/ (Unbounded Black +
JetBrains Mono Bold, SIL OFL).

Почему два файла на статью, а не один: русская страница и английская — это
две разные страницы с разными og:image. Одна обложка на обе означала бы, что
одна из аудиторий видит в превью чужой язык.

Почему не Archivo Black и не Space Mono: ни в том, ни в другом нет ни одного
кириллического глифа. Русский текст превращался в квадраты, а на сайте молча
подменялся системным Arial. Проверить: Tools/fontcheck.py.

Запуск:  python3 Tools/covers.py
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
TITLE_FONT = os.path.join(FONT_DIR, "Unbounded-Black.ttf")
MONO_FONT = os.path.join(FONT_DIR, "JetBrainsMono-Bold.ttf")

INK = (11, 11, 9)
INK_2 = (23, 23, 15)
PAPER = (242, 240, 232)
MUTED = (150, 148, 140)
YELLOW = (232, 255, 46)
BLUE = (47, 46, 240)
RED = (232, 67, 44)

# Цвет привязан к английскому тегу: он один на обе языковые версии, поэтому
# русская и английская обложки одной статьи совпадают по цвету.
ACCENT = {
    "Leadership": BLUE,
    "Management": BLUE,
    "Case Study": RED,
    "Startups": YELLOW,
    "Consulting": BLUE,
    "Automation & AI": YELLOW,
    "Web Development": RED,
    "Pricing": YELLOW,
    "Hiring": RED,
    "Project Management": BLUE,
}

FOOTER = {"ru": "GANZA CONSULTING — БЛОГ", "en": "GANZA CONSULTING — BLOG"}

W, H = 1200, 630


def short_title(h1):
    """Ударная часть заголовка — всё до первого «:», «(» или «?»."""
    m = re.split(r"[:(]", h1, maxsplit=1)[0]
    if "?" in h1 and len(m) > len(h1.split("?")[0]):
        m = h1.split("?")[0] + "?"
    return m.strip().rstrip(",").upper()


def blob(size, colour, alpha):
    """Мягкое радиальное свечение — то же, что на сайте под стеклом."""
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


def backdrop(accent):
    """Фон: вертикальный градиент плюс два цветных свечения."""
    img = Image.new("RGB", (W, H), INK)
    grad = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        grad.line([(0, y), (W, y)],
                  fill=tuple(int(INK_2[i] + (INK[i] - INK_2[i]) * t) for i in range(3)))
    for colour, alpha, pos, size in (
        (accent, 150, (-120, -180), 760),
        (BLUE if accent is not BLUE else RED, 80, (W - 460, H - 300), 640),
    ):
        tint, mask = blob(size, colour, alpha)
        img.paste(tint, pos, mask)
    return img


def chip(d, x, y, label, accent, size=21):
    """Скруглённый чип с моно-подписью. Возвращает свою ширину."""
    mono = ImageFont.truetype(MONO_FONT, size)
    tw = d.textlength(label, font=mono)
    d.rounded_rectangle([x, y, x + tw + 40, y + 42], radius=21,
                        fill=accent + (235,), outline=(255, 255, 255, 90), width=1)
    d.text((x + 20, y + 10), label, font=mono,
           fill=INK if accent is not BLUE else PAPER)
    return tw + 40


def build_cover(slug, lang, tag_en, tag, title):
    """Одна обложка. Unbounded шире Archivo Black, поэтому нижняя граница
    кегля опущена с 38 до 34: длинные русские заголовки иначе не влезают
    в три строки и обрезаются."""
    accent = ACCENT.get(tag_en, BLUE)
    img = backdrop(accent)
    d = ImageDraw.Draw(img, "RGBA")

    # тонкая внутренняя линия — край стекла
    d.rounded_rectangle([18, 18, W - 19, H - 19], radius=26,
                        outline=(255, 255, 255, 38), width=2)

    chip(d, 66, 74, tag.upper(), accent)

    size = 72
    while size > 34:
        f = ImageFont.truetype(TITLE_FONT, size)
        if len(wrap(d, title, f, W - 150)) <= 3:
            break
        size -= 3
    f = ImageFont.truetype(TITLE_FONT, size)
    lines = wrap(d, title, f, W - 150)[:3]
    lh = int(size * 1.24)
    y = 205 + (3 - len(lines)) * lh // 2
    for line in lines:
        d.text((68, y), line, font=f, fill=PAPER)
        y += lh

    small = ImageFont.truetype(MONO_FONT, 19)
    d.rounded_rectangle([68, 530, 138, 548], radius=9, fill=accent + (235,))
    d.text((156, 528), FOOTER[lang], font=small, fill=MUTED)

    out = os.path.join(ROOT, "assets", "img", "blog", f"{slug}-cover-{lang}.png")
    img.save(out, optimize=True)
    return out, size, len(lines)


SITE_CARD = {
    "ru": dict(eyebrow="НЕЗАВИСИМАЯ КОНСАЛТИНГОВАЯ СТУДИЯ",
               line="КОНСАЛТИНГ · АВТОМАТИЗАЦИЯ И ИИ · УПРАВЛЕНИЕ ПРОЕКТАМИ",
               claim="БЕЗ ШАБЛОНОВ. БЕЗ ВОДЫ."),
    "en": dict(eyebrow="INDEPENDENT CONSULTING STUDIO",
               line="CONSULTING · AUTOMATION & AI · PROJECT MANAGEMENT",
               claim="NO TEMPLATES. NO FLUFF."),
}


def build_site_card(lang):
    """Общая карточка сайта — та, что уходит в превью главной и всех
    страниц без своей обложки."""
    t = SITE_CARD[lang]
    img = backdrop(BLUE)
    d = ImageDraw.Draw(img, "RGBA")
    d.rounded_rectangle([18, 18, W - 19, H - 19], radius=26,
                        outline=(255, 255, 255, 38), width=2)

    chip(d, 66, 74, t["eyebrow"], YELLOW, size=19)

    f = ImageFont.truetype(TITLE_FONT, 76)
    d.text((68, 196), "GANZA", font=f, fill=PAPER)
    d.text((68, 300), "CONSULTING", font=f, fill=PAPER)

    small = ImageFont.truetype(MONO_FONT, 19)
    # Строка направлений по-русски длиннее английской — при переполнении
    # кегль уменьшается, а не обрезается текст.
    size = 19
    while size > 13 and d.textlength(t["line"], font=small) > W - 136:
        size -= 1
        small = ImageFont.truetype(MONO_FONT, size)
    d.text((68, 446), t["line"], font=small, fill=(255, 255, 255, 150))

    tiny = ImageFont.truetype(MONO_FONT, 19)
    d.rounded_rectangle([68, 534, 138, 552], radius=9, fill=YELLOW + (235,))
    d.text((156, 532), t["claim"], font=tiny, fill=MUTED)

    out = os.path.join(ROOT, "assets", "img", f"og-cover-{lang}.png")
    img.save(out, optimize=True)
    return out


def build_thumbs(width=760):
    """Маленькие WebP для списка блога — 1200px PNG нужны только соцсетям,
    отдавать их списком из семнадцати штук стоит около 450 КБ."""
    base = os.path.join(ROOT, "assets", "img", "blog")
    saved = 0
    for f in sorted(os.listdir(base)):
        if not f.endswith("-cover-ru.png") and not f.endswith("-cover-en.png"):
            continue
        src = os.path.join(base, f)
        dst = src.replace("-cover-", "-card-").replace(".png", ".webp")
        im = Image.open(src)
        im = im.resize((width, round(width * im.height / im.width)), Image.LANCZOS)
        im.save(dst, "WEBP", quality=82, method=6)
        saved += os.path.getsize(src) - os.path.getsize(dst)
    print(f"миниатюры записаны, сэкономлено {saved // 1024} КБ на списке")


def sweep():
    """Убирает одноязычные файлы прошлой схемы, чтобы в репозитории не
    остались обложки, на которые уже никто не ссылается."""
    base = os.path.join(ROOT, "assets", "img", "blog")
    gone = 0
    for f in sorted(os.listdir(base)):
        if re.fullmatch(r".+-(cover\.png|card\.webp)", f):
            os.remove(os.path.join(base, f))
            gone += 1
    old = os.path.join(ROOT, "assets", "img", "og-cover.png")
    if os.path.exists(old):
        os.remove(old)
        gone += 1
    if gone:
        print(f"удалено файлов старой схемы: {gone}")


def main():
    for f in (TITLE_FONT, MONO_FONT):
        if not os.path.exists(f):
            raise SystemExit(f"нет шрифта {f} — см. README")
    for post in load_posts():
        for lang in cfg.LANGS:
            title = short_title(post["h1"][lang])
            _, size, lines = build_cover(post["slug"], lang, post["tag"]["en"],
                                         post["tag"][lang], title)
            print(f"{post['slug']:<40} {lang}  {size:>3}px / {lines} стр — {title[:38]}")
    for lang in cfg.LANGS:
        print("карточка сайта:", os.path.basename(build_site_card(lang)))
    sweep()
    build_thumbs()


if __name__ == "__main__":
    main()
