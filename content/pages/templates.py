# -*- coding: utf-8 -*-
"""Хаб шаблонов и чек-листов."""
from core.pages import crumbs

TITLE = {"en": "Templates and checklists", "ru": "Шаблоны и чек-листы"}


def schema(ctx):
    return crumbs(ctx, (TITLE[ctx.lang], "templates/"))


PAGE = dict(
    slug="templates/",
    order=8,
    nav_key="",
    builder=False,
    title={"en": "Templates and checklists — Ganza Consulting",
           "ru": "Шаблоны и чек-листы — Ganza Consulting"},
    description={
        "en": "An automation brief and two checklists, assembled from practice, PRINCE2, LeSS and GOST 34.602. Open, free, printable.",
        "ru": "Шаблон ТЗ и два чек-листа, собранные из практики, PRINCE2, LeSS и ГОСТ 34.602. Открыто, бесплатно, для печати.",
    },
    hero={
        "eyebrow": {"en": "TEMPLATES", "ru": "ШАБЛОНЫ"},
        "h1": {"en": "TEMPLATES AND CHECKLISTS", "ru": "ШАБЛОНЫ И ЧЕК-ЛИСТЫ"},
        "lead": {"en": "The working documents I use myself. Nothing to hand over in exchange.",
                 "ru": "Заготовки, которыми я пользуюсь сам. Ничего не нужно оставлять взамен."},
    },
    keywords={
        "en": "automation brief template, project checklists, definition of done, PRINCE2 tolerances, supplier checklist",
        "ru": "шаблон тз автоматизации, чек-листы для проектов, определение готовности, допуски PRINCE2, выбор подрядчика",
    },
    schema=schema,
    sections=[("blocks", "templates-index")],
)
