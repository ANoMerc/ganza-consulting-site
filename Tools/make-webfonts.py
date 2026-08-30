#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Режет шрифты на подмножества и пакует в woff2 для assets/src/fonts/.

Запускается вручную и редко — только когда меняются сами шрифты. Поэтому
fonttools и brotli нужны здесь, а не в сборке сайта: у build.py по-прежнему
одна зависимость, Pillow.

    pip install fonttools brotli
    python3 Tools/make-webfonts.py

Зачем свои файлы вместо Google Fonts. Прошлый набор ломался ровно так:
Archivo Black и Space Mono раздавались с чужого CDN, кириллицы в них не было,
и никто этого не видел — браузер молча подставлял Arial. Свои файлы в
репозитории проверяются скриптом (Tools/fontcheck.py) и не могут измениться
без коммита. Заодно с сайта уходят два запроса на чужой домен.

Латиница и кириллица режутся в разные файлы с unicode-range: русский
посетитель не скачивает латинский набор, английский — кириллический.
"""
import os
import sys

try:
    from fontTools import subset
    from fontTools.ttLib import TTFont
    import brotli  # noqa: F401  проверка, что woff2 вообще соберётся
except ImportError:
    raise SystemExit("нужны fonttools и brotli:  pip install fonttools brotli")

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "fonts")
OUT = os.path.join(os.path.dirname(HERE), "assets", "src", "fonts")

# Диапазоны шире гугловских в одном месте: стрелка U+2192 у них не входит
# ни в один набор, а на сайте она стоит в каждой кнопке.
RANGES = {
    "latin": ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,"
              "U+2000-206F,U+2074,U+20AC,U+2122,U+2190-21FF,U+2212,U+2215,U+FEFF,U+FFFD"),
    "cyrillic": "U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116",
}

JOBS = [
    ("Unbounded-Black.ttf", "unbounded-900"),
    ("JetBrainsMono-Bold.ttf", "jetbrains-mono-700"),
    ("JetBrainsMono-Regular.ttf", "jetbrains-mono-400"),
]


def ranges_to_codes(spec):
    codes = []
    for part in spec.split(","):
        part = part.strip().replace("U+", "")
        if "-" in part:
            a, b = part.split("-")
            codes.extend(range(int(a, 16), int(b, 16) + 1))
        else:
            codes.append(int(part, 16))
    return codes


def main():
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for src_name, stem in JOBS:
        src = os.path.join(SRC, src_name)
        if not os.path.exists(src):
            print(f"пропущен (нет файла): {src_name}")
            continue
        for subset_name, spec in RANGES.items():
            font = TTFont(src)
            opts = subset.Options()
            opts.layout_features = ["*"]
            opts.desubroutinize = True
            opts.drop_tables += ["DSIG"]
            opts.notdef_outline = True
            s = subset.Subsetter(options=opts)
            s.populate(unicodes=ranges_to_codes(spec))
            s.subset(font)
            font.flavor = "woff2"
            dst = os.path.join(OUT, f"{stem}-{subset_name}.woff2")
            font.save(dst)
            size = os.path.getsize(dst)
            total += size
            print(f"{os.path.basename(dst):<38} {size / 1024:6.1f} КБ")
    print(f"\nвсего {total / 1024:.0f} КБ в assets/src/fonts/")
    print("не забудьте перебрать сборку: python3 Tools/build.py")


if __name__ == "__main__":
    sys.exit(main())
