# -*- coding: utf-8 -*-
"""Направление: управление проектами. Данные — в content/services/project-management.py."""
from core.services import schema_for

TITLE = {"en": "Project management", "ru": "Управление проектами"}
DESC = {
    "en": "Getting a stuck project back to a shared version of reality: the real status, a written definition of done, tolerances, and a decision log you keep.",
    "ru": "Возврат застрявшего проекта к общей картине: фактический статус, письменное определение готовности, допуски и журнал решений, который остаётся у вас.",
}

PAGE = dict(
    slug="services/project-management/",
    order=23,
    nav_key="services",
    builder=False,
    title={
        "en": "Project Management — Ganza Consulting",
        "ru": "Управление проектами — Ganza Consulting",
    },
    description={
        "en": "For rollouts stuck between departments: the actual status, the undone work named out loud, PRINCE2 tolerances, and a decision log you keep running.",
        "ru": "Для внедрений, застрявших между отделами: фактический статус, названное вслух недоделанное, допуски по PRINCE2 и журнал решений, который вы ведёте сами.",
    },
    hero={
        "eyebrow": {"en": "SERVICES · PROJECT MANAGEMENT", "ru": "УСЛУГИ · УПРАВЛЕНИЕ ПРОЕКТАМИ"},
        "h1": {"en": "PROJECT MANAGEMENT", "ru": "УПРАВЛЕНИЕ ПРОЕКТАМИ"},
        "lead": {
            "en": "Projects rarely fail on the work. They fail because \"done\" means a different thing to each side, and nobody wrote down which one counts.",
            "ru": "Проекты редко проваливаются на работе. Они проваливаются потому, что «готово» у каждой стороны своё, и никто не записал, какое из них считается.",
        },
    },
    keywords={
        "en": "project management consultant, stuck project recovery, PRINCE2 tolerances, "
              "definition of done, ERP rollout management, decision log",
        "ru": "управление проектами консультант, спасение проекта, допуски PRINCE2, "
              "определение готовности, управление внедрением ERP, журнал решений",
    },
    schema=schema_for("project-management", TITLE, DESC),
    sections=[("service", "project-management"), ("fragment", "contact-form")],
)
