# -*- coding: utf-8 -*-
"""Политика конфиденциальности. Текст — в content/blocks/privacy.py."""
from core.pages import crumbs

TITLE = {"en": "Privacy Policy", "ru": "Политика конфиденциальности"}


def schema(ctx):
    return crumbs(ctx, (TITLE[ctx.lang], "privacy/"))


PAGE = dict(
    slug="privacy/",
    order=9,
    nav_key="",
    builder=False,
    title={
        "en": "Privacy Policy — Ganza Consulting",
        "ru": "Политика конфиденциальности — Ganza Consulting",
    },
    description={
        "en": "What this site collects, what it does not, where the data is kept, "
              "how long, and how to have it removed. No cookies, no third-party trackers.",
        "ru": "Что этот сайт собирает, чего не собирает, где данные хранятся, "
              "сколько и как их удалить. Без cookie и чужих счётчиков.",
    },
    hero={
        "eyebrow": {"en": "PRIVACY", "ru": "КОНФИДЕНЦИАЛЬНОСТЬ"},
        "h1": TITLE,
        "lead": {
            "en": "Written against what the code actually does, not against a template.",
            "ru": "Написана по тому, что делает код, а не по шаблону.",
        },
    },
    schema=schema,
    sections=[("blocks", "privacy")],
)
