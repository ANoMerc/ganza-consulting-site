# -*- coding: utf-8 -*-
"""«За что я берусь и за что нет». Текст — в content/blocks/what-i-take.py."""
from core.pages import crumbs

TITLE = {"en": "What I take on and what I decline",
         "ru": "За что я берусь и за что нет"}


def schema(ctx):
    return crumbs(ctx, (TITLE[ctx.lang], "what-i-take/"))


PAGE = dict(
    slug="what-i-take/",
    order=3,
    nav_key="",
    builder=False,
    title={
        "en": "What I take on and what I decline — Ganza Consulting",
        "ru": "За что я берусь и за что нет — Ganza Consulting",
    },
    description={
        "en": "Four conditions under which I take a problem on, four under which I decline, and what to do instead — so it doesn't take three calls to find out.",
        "ru": "Четыре условия, при которых я берусь за задачу, и четыре, при которых отказываюсь — с объяснением почему и что делать вместо этого.",
    },
    hero={
        "eyebrow": {"en": "BEFORE YOU WRITE", "ru": "ДО ТОГО, КАК НАПИСАТЬ"},
        "h1": {"en": "WHAT I TAKE ON AND WHAT I DECLINE",
               "ru": "ЗА ЧТО Я БЕРУСЬ И ЗА ЧТО НЕТ"},
        "lead": {
            "en": "Not about difficulty. About the conditions under which no amount of "
                  "work produces a result.",
            "ru": "Не про сложность. Про условия, при которых работа не даст результата, "
                  "сколько бы её ни было.",
        },
    },
    keywords={
        "en": "consultant selection criteria, when not to hire a consultant, "
              "consulting engagement conditions",
        "ru": "когда не нужен консультант, критерии работы с консультантом, "
              "условия работы с подрядчиком",
    },
    schema=schema,
    sections=[("blocks", "what-i-take")],
)
