# -*- coding: utf-8 -*-
"""Направление: автоматизация. Данные — в content/services/automation.py."""
from core.services import schema_for

TITLE = {"en": "Process automation", "ru": "Автоматизация процессов"}
DESC = {
    "en": "Removing manual routine from a process that already works: what gets automated, what deliberately stays with people, and what you keep afterwards.",
    "ru": "Снятие ручной рутины с процесса, который уже работает: что автоматизируется, что сознательно остаётся за людьми и что остаётся у вас после.",
}

PAGE = dict(
    slug="services/automation/",
    order=20,
    nav_key="services",
    builder=False,
    title={
        "en": "Process Automation — Ganza Consulting",
        "ru": "Автоматизация процессов — Ganza Consulting",
    },
    description={
        "en": "What automation actually costs, which part of a process should stay manual, and what you keep when the work is done. No platform lock-in.",
        "ru": "Сколько стоит автоматизация, какую часть процесса разумнее оставить людям и что остаётся у вас после работы. Без привязки к моей инфраструктуре.",
    },
    hero={
        "eyebrow": {"en": "SERVICES · AUTOMATION", "ru": "УСЛУГИ · АВТОМАТИЗАЦИЯ"},
        "h1": {"en": "PROCESS AUTOMATION", "ru": "АВТОМАТИЗАЦИЯ ПРОЦЕССОВ"},
        "lead": {
            "en": "Automating a broken process makes it break faster. So the first question is not what to automate but whether this process is ready to be.",
            "ru": "Автоматизация сломанного процесса ломает его быстрее. Поэтому первый вопрос не «что автоматизировать», а «готов ли этот процесс к автоматизации».",
        },
    },
    keywords={
        "en": "business process automation, automation consultant, n8n implementation, "
              "automate or hire, small business automation",
        "ru": "автоматизация бизнес-процессов, консультант по автоматизации, внедрение n8n, "
              "автоматизировать или нанять, автоматизация малого бизнеса",
    },
    schema=schema_for("automation", TITLE, DESC),
    sections=[("service", "automation"), ("fragment", "contact-form")],
)
