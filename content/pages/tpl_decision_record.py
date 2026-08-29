# -*- coding: utf-8 -*-
"""Шаблон протокола решения. Текст — в content/blocks/tpl-decision-record.py."""
from core.pages import crumbs

TITLE = {"en": "Decision record template", "ru": "Шаблон протокола решения"}


def schema(ctx):
    return crumbs(ctx,
                  ({"en": "Templates", "ru": "Шаблоны"}[ctx.lang], "templates/"),
                  (TITLE[ctx.lang], "templates/decision-record/"))


PAGE = dict(
    slug="templates/decision-record/",
    order=13,
    nav_key="",
    builder=False,
    title={
        "en": "Decision Record Template — Ganza Consulting",
        "ru": "Шаблон протокола решения — Ganza Consulting",
    },
    description={
        "en": "Who said what, who got which task, what was decided — and what counts as done. For asynchronous teams.",
        "ru": "Кто что сказал, кому что поручено, что решено и что считается сделанным. Для асинхронных команд.",
    },
    hero={
        "eyebrow": {"en": "TEMPLATE", "ru": "ШАБЛОН"},
        "h1": {"en": "DECISION RECORD", "ru": "ПРОТОКОЛ РЕШЕНИЯ"},
        "lead": {
            "en": "A meeting without a record everyone can see produces the same four arguments every time.",
            "ru": "Встреча без записи, которую видят все, каждый раз порождает одни и те же четыре реплики.",
        },
    },
    keywords={
        "en": "decision record template, meeting minutes template, async team communication, definition of done, undone work",
        "ru": "шаблон протокола встречи, протокол решений, асинхронная команда, определение готовности, недоделанная работа",
    },
    schema=schema,
    sections=[("blocks", "tpl-decision-record")],
)
