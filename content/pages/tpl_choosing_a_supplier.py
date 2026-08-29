# -*- coding: utf-8 -*-
"""Чек-лист выбора подрядчика. Текст — в content/blocks/tpl-choosing-supplier.py."""
from core.pages import crumbs

TITLE = {'en': 'Choosing a supplier checklist', 'ru': 'Чек-лист выбора подрядчика'}


def schema(ctx):
    return crumbs(ctx,
                  ({"en": "Templates", "ru": "Шаблоны"}[ctx.lang], "templates/"),
                  (TITLE[ctx.lang], "templates/choosing-a-supplier/"))


PAGE = dict(
    slug="templates/choosing-a-supplier/",
    order=12,
    nav_key="",
    builder=False,
    title={'en': 'Choosing a Supplier Checklist — Ganza Consulting', 'ru': 'Чек-лист выбора подрядчика — Ganza Consulting'},
    description={'en': 'Five questions with good and bad answers, four continuity guarantees to demand, and the signs of inflated scope.', 'ru': 'Пять вопросов с хорошими и плохими ответами, четыре гарантии непрерывности и признаки раздутого объёма.'},
    hero={
        "eyebrow": {'en': 'CHECKLIST', 'ru': 'ЧЕК-ЛИСТ'},
        "h1": {'en': 'CHOOSING A SUPPLIER', 'ru': 'ВЫБОР ПОДРЯДЧИКА'},
        "lead": {'en': 'What to ask before signing, and what a bad answer sounds like.', 'ru': 'Что спросить до подписания и как звучит плохой ответ.'},
    },
    keywords={'en': 'choosing a consultant, supplier checklist, continuity guarantees, questions before signing', 'ru': 'выбор подрядчика, чек-лист консультанта, гарантии непрерывности, вопросы до подписания'},
    schema=schema,
    sections=[("blocks", "tpl-choosing-supplier")],
)
