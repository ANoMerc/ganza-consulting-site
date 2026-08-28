#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Создать новую статью, кейс или страницу — одной командой.

    python3 Tools/new.py post  kak-vybrat-podryadchika
    python3 Tools/new.py case  avtomatizatsiya-sklada
    python3 Tools/new.py page  contacts

Создаёт заготовку в content/ со всеми обязательными полями и подсказками,
затем сразу пересобирает сайт, чтобы новая страница появилась в меню,
sitemap и перелинковке. Дальше остаётся только заполнить текст и запустить
python3 Tools/build.py ещё раз.
"""
import datetime
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import config as cfg

TODAY = datetime.date.today().isoformat()

POST = '''# -*- coding: utf-8 -*-
POST = dict(
    date="{today}",
    updated="{today}",
    tag={{"en": "Consulting", "ru": "Консалтинг"}},

    # <title> — до 60 символов, иначе обрежется в выдаче
    title={{"en": "TODO en title", "ru": "TODO ru заголовок"}},
    # <h1> — может быть длиннее и подробнее, чем title
    h1={{"en": "TODO en headline", "ru": "TODO ru заголовок статьи"}},
    # подзаголовок под h1
    dek={{"en": "TODO en standfirst.", "ru": "TODO ru подзаголовок."}},
    # meta description — 140–158 символов
    description={{"en": "TODO en description.", "ru": "TODO ru описание."}},
    keywords={{"en": "todo, keywords", "ru": "todo, ключевые слова"}},

    hashtags=["Consulting"],
    related=[],          # slug'и других статей — блок «по теме»

    body={{
        "en": [
            ("p", "Answer the question in the first three paragraphs."),
            ("h2", "First section"),
            ("p", "TODO"),
        ],
        "ru": [
            ("p", "Ответ на вопрос — в первых трёх абзацах."),
            ("h2", "Первый раздел"),
            ("p", "TODO"),
        ],
    }},

    takeaways={{
        "en": ["TODO"],
        "ru": ["TODO"],
    }},

    faq={{
        "en": [("TODO question?", "TODO answer.")],
        "ru": [("TODO вопрос?", "TODO ответ.")],
    }},
)
'''

CASE = '''# -*- coding: utf-8 -*-
CASE = dict(
    order={order},
    accent="{accent}",          # yellow | blue | red
    client={{"en": "Client: TODO", "ru": "Клиент: TODO"}},
    stat={{"en": "TODO", "ru": "TODO"}},            # одна цифра, крупно
    title={{"en": "TODO", "ru": "TODO"}},
    problem={{
        "en": "TODO what was wrong.",
        "ru": "TODO что было не так.",
    }},
    did={{
        "en": "TODO what we did.",
        "ru": "TODO что сделали.",
    }},
    result={{"en": "TODO measurable result", "ru": "TODO измеримый результат"}},
    tags=["TODO"],
)
'''

PAGE = '''# -*- coding: utf-8 -*-
"""TODO: одна строка о том, зачем эта страница."""
PAGE = dict(
    slug="{slug}/",
    order={order},
    nav_key="",          # ключ из cfg.NAV, если страница должна быть в меню
    title={{"en": "TODO — Ganza Consulting", "ru": "TODO — Ganza Consulting"}},
    description={{"en": "TODO en, 140–158 chars.", "ru": "TODO ru, 140–158 символов."}},
    keywords={{"en": "todo", "ru": "todo"}},
    sections=[
        # ("fragment", "имя-файла-из-content/fragments")
        # ("cases", 3) ("posts", 3) ("services_teaser", None)
        ("fragment", "how-we-work"),
    ],
)
'''


def slugify(s):
    return re.sub(r"[^a-z0-9-]+", "-", s.lower()).strip("-")


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("post", "case", "page"):
        print(__doc__)
        sys.exit(1)

    kind, slug = sys.argv[1], slugify(sys.argv[2])
    folder = {"post": "posts", "case": "cases", "page": "pages"}[kind]
    path = os.path.join(cfg.CONTENT, folder, slug + ".py")

    if os.path.exists(path):
        print(f"✗ {path} уже существует")
        sys.exit(1)

    existing = len([f for f in os.listdir(os.path.join(cfg.CONTENT, folder))
                    if f.endswith(".py") and not f.startswith("_")])
    if kind == "post":
        text = POST.format(today=TODAY)
    elif kind == "case":
        text = CASE.format(order=existing + 1,
                           accent=["yellow", "blue", "red"][existing % 3])
    else:
        text = PAGE.format(slug=slug, order=existing + 1)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)
    print(f"✓ создано  {os.path.relpath(path, cfg.ROOT)}")

    if kind == "post":
        print("  дальше: заполнить текст → python3 Tools/covers.py → python3 Tools/build.py")
    else:
        print("  дальше: заполнить текст → python3 Tools/build.py")

    print("\nпересобираю сайт с заготовкой…\n")
    subprocess.run([sys.executable, os.path.join(cfg.ROOT, "Tools", "build.py")], check=False)


if __name__ == "__main__":
    main()
