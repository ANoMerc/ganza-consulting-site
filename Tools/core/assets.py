# -*- coding: utf-8 -*-
"""ЯДРО · Сборка ассетов.

Авторские стили и скрипты лежат в assets/src/. Сюда они попадают как список
файлов, отсюда выходят склеенными в assets/build/. Смысл ровно один: раньше
страница тянула четыре блокирующих CSS-файла и два скрипта, теперь один и
один.

Минифицируем только CSS, и то консервативно — убираем комментарии и лишние
пробелы. JS не трогаем: без разбора синтаксиса это способ однажды сломать
продуктив ради двух килобайт, а гзип на отдаче и так делает основную работу.
Никаких зависимостей у сборки от этого не появляется.
"""
import hashlib
import os
import re
import shutil

from . import config as cfg

SRC = os.path.join(cfg.ROOT, "assets", "src")
OUT = os.path.join(cfg.ROOT, "assets", "build")

# ---------------------------------------------------------------------------
# Шрифты
# ---------------------------------------------------------------------------
# Свои файлы вместо чужого CDN. Причина не в скорости: прошлый набор шрифтов
# раздавался Google Fonts и не содержал кириллицы, из-за чего весь русский
# сайт набирался системным Arial, и заметить это было нечем. Свои файлы
# лежат в репозитории и проверяются скриптом Tools/fontcheck.py.
#
# Латиница и кириллица — разные файлы с unicode-range: русский посетитель не
# качает латинский набор, английский не качает кириллический. Режет и пакует
# Tools/make-webfonts.py, вручную и редко.
LATIN = ("U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,"
         "U+2000-206F,U+2074,U+20AC,U+2122,U+2190-21FF,U+2212,U+2215,U+FEFF,U+FFFD")
CYRILLIC = "U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116"

# (файл, семейство, начертание, диапазон)
FONT_FACES = [
    ("unbounded-900-cyrillic.woff2",     "Unbounded",      "900",       CYRILLIC),
    ("unbounded-900-latin.woff2",        "Unbounded",      "900",       LATIN),
    ("jetbrains-mono-400-cyrillic.woff2", "JetBrains Mono", "400",      CYRILLIC),
    ("jetbrains-mono-400-latin.woff2",    "JetBrains Mono", "400",      LATIN),
    ("jetbrains-mono-700-cyrillic.woff2", "JetBrains Mono", "700",      CYRILLIC),
    ("jetbrains-mono-700-latin.woff2",    "JetBrains Mono", "700",      LATIN),
    ("inter-var-cyrillic.woff2",          "Inter",         "100 900",   CYRILLIC),
    ("inter-var-latin.woff2",             "Inter",         "100 900",   LATIN),
]

# Что предзагружать в <head> — по языку страницы: заголовок и текст первого
# экрана, и только они. Предзагружать всё — значит соревноваться с
# собственным CSS за ту же полосу.
PRELOAD = {
    "ru": ["unbounded-900-cyrillic.woff2", "inter-var-cyrillic.woff2"],
    "en": ["unbounded-900-latin.woff2", "inter-var-latin.woff2"],
}

# Порядок важен: glass.css — снимаемый слой оформления и идёт последним.
# lowpower.css последним: он снимает оформление, а не добавляет.
CSS_BUNDLE = ["base.css", "builder.css", "blog.css", "glass.css", "lowpower.css"]

# core грузится везде; остальные — только там, где нужны.
JS_BUNDLES = {
    "core": ["site.js", "analytics.js"],
    "builder": ["builder.js"],
    "form": ["form.js"],
}


def _minify_css(css):
    css = re.sub(r"/\*[\s\S]*?\*/", "", css)          # комментарии
    css = re.sub(r"\s*\n\s*", "\n", css)              # отступы в начале строк
    css = re.sub(r"\n{2,}", "\n", css)                # пустые строки
    css = re.sub(r"\s*([{};:,>])\s*", r"\1", css)     # пробелы вокруг разделителей
    css = re.sub(r";}", "}", css)                     # последняя точка с запятой
    return css.strip()


def _hash(text):
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]


def build():
    """Склеивает бандлы и возвращает {имя: путь относительно assets/}."""
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        os.remove(os.path.join(OUT, f))

    out = {}

    # Шрифты копируются в build/ с хешем в имени и объявляются @font-face
    # в начале бандла. Оба лежат в одной папке, поэтому в url() достаточно
    # имени файла — относительные пути внутри build/ никогда не разъедутся.
    fonts = {}
    for fname, family, weight, urange in FONT_FACES:
        src = os.path.join(SRC, "fonts", fname)
        digest = hashlib.sha1(open(src, "rb").read()).hexdigest()[:8]
        stem, ext = os.path.splitext(fname)
        hashed = f"{stem}.{digest}{ext}"
        shutil.copyfile(src, os.path.join(OUT, hashed))
        fonts[fname] = hashed
    out["preload_fonts"] = {lang: [f"build/{fonts[f]}" for f in files]
                            for lang, files in PRELOAD.items()}

    faces = "\n".join(
        "@font-face{font-family:'%s';font-style:normal;font-weight:%s;"
        "font-display:swap;src:url(%s) format('woff2');unicode-range:%s;}"
        % (family, weight, fonts[fname], urange)
        for fname, family, weight, urange in FONT_FACES
    )

    css = "\n".join(
        open(os.path.join(SRC, "css", f), encoding="utf-8").read() for f in CSS_BUNDLE
    )
    css = faces + "\n" + _minify_css(css)
    name = f"site.{_hash(css)}.css"
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(css)
    out["css"] = f"build/{name}"

    for bundle, files in JS_BUNDLES.items():
        js = "\n;\n".join(
            open(os.path.join(SRC, "js", f), encoding="utf-8").read() for f in files
        )
        name = f"{bundle}.{_hash(js)}.js"
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(js)
        out[bundle] = f"build/{name}"

    return out


def report(built):
    src_bytes = sum(
        os.path.getsize(os.path.join(SRC, kind, f))
        for kind, files in (("css", CSS_BUNDLE),
                            ("js", [f for fs in JS_BUNDLES.values() for f in fs]))
        for f in files
    )
    out_bytes = sum(os.path.getsize(os.path.join(OUT, f))
                    for f in os.listdir(OUT) if not f.endswith(".woff2"))
    font_bytes = sum(os.path.getsize(os.path.join(OUT, f))
                     for f in os.listdir(OUT) if f.endswith(".woff2"))
    return (f"ассеты: {len(CSS_BUNDLE)}+{sum(len(v) for v in JS_BUNDLES.values())} файлов "
            f"→ {len(built) - 1} бандла · {src_bytes // 1024} → {out_bytes // 1024} КБ · "
            f"шрифты {len(FONT_FACES)} файлов, {font_bytes // 1024} КБ "
            f"(на язык качается около половины)")
