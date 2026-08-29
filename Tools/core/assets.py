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

from . import config as cfg

SRC = os.path.join(cfg.ROOT, "assets", "src")
OUT = os.path.join(cfg.ROOT, "assets", "build")

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

    css = "\n".join(
        open(os.path.join(SRC, "css", f), encoding="utf-8").read() for f in CSS_BUNDLE
    )
    css = _minify_css(css)
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
    out_bytes = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT))
    return (f"ассеты: {len(CSS_BUNDLE)}+{sum(len(v) for v in JS_BUNDLES.values())} файлов "
            f"→ {len(built)} бандла · {src_bytes // 1024} → {out_bytes // 1024} КБ")
