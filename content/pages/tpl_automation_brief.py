# -*- coding: utf-8 -*-
"""Шаблон ТЗ на автоматизацию. Текст — в content/blocks/tpl-automation-brief.py."""
from core.pages import crumbs

TITLE = {'en': 'Automation brief template', 'ru': 'Шаблон ТЗ на автоматизацию'}


def schema(ctx):
    return crumbs(ctx,
                  ({"en": "Templates", "ru": "Шаблоны"}[ctx.lang], "templates/"),
                  (TITLE[ctx.lang], "templates/automation-brief/"))


PAGE = dict(
    slug="templates/automation-brief/",
    order=10,
    nav_key="",
    builder=False,
    title={'en': 'Automation Brief Template — Ganza Consulting', 'ru': 'Шаблон ТЗ на автоматизацию — Ganza Consulting'},
    description={'en': 'Nine sections for automating one process: fitness scoring, definition of done, tolerances and what you keep afterwards.', 'ru': 'Девять разделов на автоматизацию одного процесса: пригодность, определение готовности, допуски и что остаётся у вас.'},
    hero={
        "eyebrow": {'en': 'BRIEF TEMPLATE', 'ru': 'ШАБЛОН ТЗ'},
        "h1": {'en': 'AUTOMATION BRIEF FOR ONE PROCESS', 'ru': 'ТЗ НА АВТОМАТИЗАЦИЮ ОДНОГО ПРОЦЕССА'},
        "lead": {'en': 'Shorter than the standard, and built so that filling in the first three sections already answers the main question.', 'ru': 'Короче стандарта и устроен так, что первые три раздела уже отвечают на главный вопрос.'},
    },
    keywords={'en': 'automation brief template, technical specification for automation, GOST 34.602, definition of done, PRINCE2 tolerances', 'ru': 'шаблон тз на автоматизацию, техническое задание автоматизация, ГОСТ 34.602, определение готовности, допуски PRINCE2'},
    schema=schema,
    sections=[("blocks", "tpl-automation-brief")],
)
