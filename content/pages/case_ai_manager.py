# -*- coding: utf-8 -*-
"""Кейс «ИИ-менеджер вместо найма» как заполненный шаблон ТЗ.

Текст — в content/blocks/case-ai-manager.py.
"""
from core.pages import crumbs

TITLE = {"en": "AI manager instead of a hire",
         "ru": "ИИ-менеджер вместо найма"}


def schema(ctx):
    return crumbs(ctx,
                  ({"en": "Cases", "ru": "Кейсы"}[ctx.lang], "cases/"),
                  (TITLE[ctx.lang], "cases/ai-manager/"))


PAGE = dict(
    slug="cases/ai-manager/",
    order=4,
    nav_key="cases",
    builder=False,
    title={
        "en": "AI Manager Instead of a Hire — the filled brief",
        "ru": "ИИ-менеджер вместо найма — заполненное ТЗ | Ganza Consulting",
    },
    description={
        "en": "A real automation brief, filled in and annotated: the 80/20 split, the fitness score, and why paid language models were ruled out.",
        "ru": "Настоящее ТЗ на автоматизацию, заполненное и с пояснениями: разделение 80/20, оценка пригодности и почему отказались от платных ИИ-моделей.",
    },
    hero={
        "eyebrow": {"en": "CASE AS A FILLED BRIEF", "ru": "КЕЙС КАК ЗАПОЛНЕННОЕ ТЗ"},
        "h1": {"en": "AI MANAGER INSTEAD OF A HIRE",
               "ru": "ИИ-МЕНЕДЖЕР ВМЕСТО НАЙМА"},
        "lead": {
            "en": "Not a story about a project — the working document behind it, with notes on why each answer is worded that way.",
            "ru": "Не рассказ о проекте, а рабочий документ по нему — с пояснениями, почему каждый ответ сформулирован именно так.",
        },
    },
    keywords={
        "en": "automation case study, filled automation brief, AI instead of hiring, n8n implementation, why not to use LLM, process automation example",
        "ru": "кейс автоматизации, заполненное тз на автоматизацию, ИИ вместо найма, внедрение n8n, почему отказались от ИИ, пример автоматизации процесса",
    },
    schema=schema,
    sections=[("blocks", "case-ai-manager")],
)
