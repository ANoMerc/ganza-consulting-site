# -*- coding: utf-8 -*-
"""Шумовой аудит по Канеману. Текст — в content/blocks/tpl-noise-audit.py."""
from core.pages import crumbs

TITLE = {"en": "Noise audit", "ru": "Шумовой аудит"}


def schema(ctx):
    return crumbs(ctx,
                  ({"en": "Templates", "ru": "Шаблоны"}[ctx.lang], "templates/"),
                  (TITLE[ctx.lang], "templates/noise-audit/"))


PAGE = dict(
    slug="templates/noise-audit/",
    order=14,
    nav_key="",
    builder=False,
    title={
        "en": "Noise Audit Template — Ganza Consulting",
        "ru": "Шумовой аудит: шаблон по Канеману — Ganza Consulting",
    },
    description={
        "en": "Measure the scatter in judgements that should agree: how to run the audit, three kinds of noise, and six decision hygiene practices.",
        "ru": "Как измерить разброс в решениях, которые должны совпадать: порядок аудита, три вида шума и шесть приёмов гигиены решений.",
    },
    hero={
        "eyebrow": {"en": "TEMPLATE", "ru": "ШАБЛОН"},
        "h1": {"en": "NOISE AUDIT", "ru": "ШУМОВОЙ АУДИТ"},
        "lead": {
            "en": "Bias is a systematic miss and can be spotted. Noise is scatter, and almost nobody measures it.",
            "ru": "Предвзятость промахивается в одну сторону, её видно. Шум — это разброс, и его почти никто не измеряет.",
        },
    },
    keywords={
        "en": "noise audit, Kahneman noise, decision hygiene, mediating assessments protocol, level noise, occasion noise, structured interviews",
        "ru": "шумовой аудит, Канеман шум, гигиена решений, протокол промежуточных оценок, разброс оценок, независимая оценка, структурированное интервью",
    },
    schema=schema,
    sections=[("blocks", "tpl-noise-audit")],
)
