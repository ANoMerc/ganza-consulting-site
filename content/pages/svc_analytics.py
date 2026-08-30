# -*- coding: utf-8 -*-
"""Направление: аналитика и данные. Данные — в content/services/analytics.py."""
from core.services import schema_for

TITLE = {"en": "Analytics and data", "ru": "Аналитика и данные"}
DESC = {
    "en": "One question, one checkable answer: consolidating scattered exports, testing the uncomfortable hypotheses, and arithmetic you can repeat yourself.",
    "ru": "Один вопрос — один проверяемый ответ: сведение разрозненных выгрузок, проверка неудобных гипотез и расчёт, который вы повторите сами.",
}

PAGE = dict(
    slug="services/analytics/",
    order=22,
    nav_key="services",
    builder=False,
    title={
        "en": "Analytics and Data — Ganza Consulting",
        "ru": "Аналитика и данные — Ganza Consulting",
    },
    description={
        "en": "A written answer with the arithmetic shown, not a sixty-slide deck: which promotion paid off, where the dip came from, whether the line of business earns.",
        "ru": "Письменный ответ с показанным расчётом вместо отчёта на шестьдесят слайдов: какая акция окупилась, откуда просадка, окупается ли направление.",
    },
    hero={
        "eyebrow": {"en": "SERVICES · ANALYTICS", "ru": "УСЛУГИ · АНАЛИТИКА"},
        "h1": {"en": "ANALYTICS AND DATA", "ru": "АНАЛИТИКА И ДАННЫЕ"},
        "lead": {
            "en": "A correct report that changes nothing is a failed report. So the work starts from the decision it has to support, not from the data that happens to exist.",
            "ru": "Верный отчёт, после которого ничего не изменилось, — это неудачный отчёт. Поэтому работа начинается с решения, которое он должен поддержать.",
        },
    },
    keywords={
        "en": "business data analysis, retail analytics consultant, promotion ROI analysis, "
              "data reconciliation, decision support analytics",
        "ru": "анализ данных для бизнеса, аналитика в ритейле, расчёт окупаемости акций, "
              "сведение данных, аналитика для принятия решений",
    },
    schema=schema_for("analytics", TITLE, DESC),
    sections=[("service", "analytics"), ("fragment", "contact-form")],
)
