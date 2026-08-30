#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверяет, что шрифты сайта покрывают все символы, которыми написан сайт.

Зачем отдельный скрипт. Шрифт без нужного глифа не падает и не ругается —
браузер молча подставляет системный, а Pillow рисует квадрат. Так и вышло:
Archivo Black и Space Mono не содержат ни одной кириллической буквы, и весь
русский сайт полгода набирался Arial и Courier New, а обложки статей были
только по-английски. Заметить это без проверки нельзя: выглядит как «шрифт
просто такой».

Запуск:  python3 Tools/fontcheck.py     (код возврата 1, если чего-то нет)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import config as cfg
from core.pages import load_posts, load_pages, load_cases, load_services

try:
    from fontTools.ttLib import TTFont
except ImportError:
    raise SystemExit("нужен fonttools:  pip install fonttools")

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
FONTS = {
    "Unbounded Black (заголовки)": "Unbounded-Black.ttf",
    "JetBrains Mono Bold (подписи)": "JetBrainsMono-Bold.ttf",
}


def coverage(path):
    t = TTFont(path)
    chars = set()
    for table in t["cmap"].tables:
        chars |= set(table.cmap.keys())
    return chars


def site_text():
    """Всё, что попадает в обложки: заголовки, теги, подписи."""
    s = set()
    for post in load_posts():
        for lang in cfg.LANGS:
            s |= set(post["h1"][lang].upper())
            s |= set(post["tag"][lang].upper())
    s |= set("GANZA CONSULTING — БЛОГ BLOG")
    s |= set("КОНСАЛТИНГ · АВТОМАТИЗАЦИЯ И ИИ · УПРАВЛЕНИЕ ПРОЕКТАМИ")
    s |= set("БЕЗ ШАБЛОНОВ. БЕЗ ВОДЫ. NO TEMPLATES. NO FLUFF.")
    s |= set("НЕЗАВИСИМАЯ КОНСАЛТИНГОВАЯ СТУДИЯ INDEPENDENT STUDIO")
    return {c for c in s if c not in "\n\r\t"}


def main():
    need = site_text()
    bad = 0
    for name, fname in FONTS.items():
        path = os.path.join(FONT_DIR, fname)
        if not os.path.exists(path):
            print(f"{name}: файла нет — {fname}")
            bad += 1
            continue
        have = coverage(path)
        missing = sorted(c for c in need if ord(c) not in have)
        if missing:
            bad += 1
            print(f"{name}: нет глифов — {''.join(missing)}")
        else:
            print(f"{name}: покрывает все {len(need)} символа сайта")
    if bad:
        print("\nОбложки нельзя собирать этими шрифтами: будут квадраты.")
        return 1
    print("\nзамечаний нет")
    return 0


if __name__ == "__main__":
    sys.exit(main())
