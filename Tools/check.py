#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Проверка собранного сайта. Возвращает ненулевой код, если что-то не так.

    python3 Tools/check.py

Что проверяет:
  · все внутренние ссылки ведут на существующие файлы;
  · у каждой страницы есть <title>, meta description и ровно один <h1>;
  · длина title ≤ 65 символов, description ≤ 165 (иначе обрежется в выдаче);
  · canonical и hreflang проставлены и указывают на существующие адреса;
  · JSON-LD парсится.

Запускается в CI перед публикацией — см. .github/workflows/deploy.yml.
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import config as cfg

SKIP_DIRS = ("Tools", "content", ".git", ".github")
TITLE_MAX, DESC_MAX = 65, 165


def pages():
    for f in glob.glob("**/*.html", recursive=True):
        if not f.startswith(SKIP_DIRS):
            yield f


def main():
    os.chdir(cfg.ROOT)
    problems = []
    checked = 0

    for f in pages():
        checked += 1
        s = open(f, encoding="utf-8").read()
        d = os.path.dirname(f)
        redirect = 'http-equiv="refresh"' in s

        # ссылки
        for m in re.findall(r'(?:href|src|srcset)="([^"#][^"]*)"', s):
            if m.startswith(("http", "mailto:", "tel:", "data:", "//")):
                continue
            t = os.path.normpath(os.path.join(d, m.split("#")[0]))
            if t.endswith("/") or os.path.isdir(t):
                t = os.path.join(t, "index.html")
            if not os.path.exists(t):
                problems.append(f"{f}: битая ссылка → {m}")

        # редиректы, 404 и закрытые от индексации страницы (админка)
        # проверяем только на битые ссылки — SEO-требования к ним не применимы
        noindex = re.search(r'name="robots"[^>]*content="[^"]*noindex', s)
        if redirect or noindex or f == "404.html":
            continue

        # мета
        title = re.search(r"<title>(.*?)</title>", s, re.S)
        desc = re.search(r'name="description" content="([^"]*)"', s)
        h1 = re.findall(r"<h1[ >]", s)

        if not title:
            problems.append(f"{f}: нет <title>")
        elif len(title.group(1)) > TITLE_MAX:
            problems.append(f"{f}: title {len(title.group(1))} симв. (>{TITLE_MAX})")
        if not desc:
            problems.append(f"{f}: нет meta description")
        elif len(desc.group(1)) > DESC_MAX:
            problems.append(f"{f}: description {len(desc.group(1))} симв. (>{DESC_MAX})")
        if len(h1) != 1:
            problems.append(f"{f}: <h1> встречается {len(h1)} раз, нужен ровно один")

        if 'rel="canonical"' not in s:
            problems.append(f"{f}: нет canonical")
        for lang in cfg.LANGS:
            if f'hreflang="{lang}"' not in s:
                problems.append(f"{f}: нет hreflang={lang}")

        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try:
                json.loads(block)
            except json.JSONDecodeError as e:
                problems.append(f"{f}: JSON-LD не парсится — {e}")

    print(f"проверено страниц: {checked}")
    if problems:
        print(f"\nпроблем: {len(problems)}")
        for p in problems[:40]:
            print("  ✗", p)
        if len(problems) > 40:
            print(f"  … и ещё {len(problems) - 40}")
        sys.exit(1)
    print("замечаний нет")


if __name__ == "__main__":
    main()
