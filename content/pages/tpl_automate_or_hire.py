# -*- coding: utf-8 -*-
"""Чек-лист: нанимать или автоматизировать. Текст — в content/blocks/tpl-automate-or-hire.py."""
from core.pages import crumbs

TITLE = {'en': 'Automate or hire checklist', 'ru': 'Чек-лист: нанимать или автоматизировать'}


def schema(ctx):
    return crumbs(ctx,
                  ({"en": "Templates", "ru": "Шаблоны"}[ctx.lang], "templates/"),
                  (TITLE[ctx.lang], "templates/automate-or-hire/"))


PAGE = dict(
    slug="templates/automate-or-hire/",
    order=11,
    nav_key="",
    builder=False,
    title={'en': 'Automate or Hire Checklist — Ganza Consulting', 'ru': 'Чек-лист: нанимать или автоматизировать — Ganza Consulting'},
    description={'en': 'Cost both sides in full, split routine from decisions, and test the routine part before anyone writes a line of code.', 'ru': 'Посчитать обе стороны целиком, отделить рутину от решений и проверить рутинную часть до первой строки кода.'},
    hero={
        "eyebrow": {'en': 'CHECKLIST', 'ru': 'ЧЕК-ЛИСТ'},
        "h1": {'en': 'AUTOMATE OR HIRE', 'ru': 'НАНИМАТЬ ИЛИ АВТОМАТИЗИРОВАТЬ'},
        "lead": {'en': 'An hour of arithmetic, before you talk to a supplier and before you open a vacancy.', 'ru': 'Час арифметики — до разговора с подрядчиком и до открытия вакансии.'},
    },
    keywords={'en': 'automate or hire, cost of an employee, automation payback, hiring checklist', 'ru': 'нанимать или автоматизировать, полная стоимость сотрудника, окупаемость автоматизации, чек-лист найма'},
    schema=schema,
    sections=[("blocks", "tpl-automate-or-hire")],
)
