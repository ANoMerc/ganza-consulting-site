# -*- coding: utf-8 -*-
"""Направление: ИИ в процессах. Данные — в content/services/ai.py."""
from core.services import schema_for

TITLE = {"en": "AI inside a process", "ru": "ИИ внутри процесса"}
DESC = {
    "en": "Where a language model genuinely helps, where a plain rule is cheaper and more reliable, and how to tell the two apart before paying for either.",
    "ru": "Где языковая модель действительно помогает, где обычное правило дешевле и надёжнее, и как отличить одно от другого до того, как платить.",
}

PAGE = dict(
    slug="services/ai/",
    order=21,
    nav_key="services",
    builder=False,
    title={
        "en": "AI Inside a Process — Ganza Consulting",
        "ru": "ИИ внутри процесса — Ganza Consulting",
    },
    description={
        "en": "Where a language model earns its cost and where a plain rule beats it. An honest fitness check before the budget, not a demo after it.",
        "ru": "Где языковая модель окупается, а где обычное правило работает лучше. Честная проверка пригодности до бюджета, а не демонстрация после.",
    },
    hero={
        "eyebrow": {"en": "SERVICES · AI", "ru": "УСЛУГИ · ИИ"},
        "h1": {"en": "AI INSIDE A PROCESS", "ru": "ИИ ВНУТРИ ПРОЦЕССА"},
        "lead": {
            "en": "Most tasks people bring to a language model are better served by a rule. My job is to say which of yours is which — including when the answer is neither.",
            "ru": "Большинство задач, которые несут языковой модели, лучше решаются правилом. Моя работа — сказать, какая из ваших какая, включая случай «ни то ни другое».",
        },
    },
    keywords={
        "en": "AI implementation consultant, LLM in business processes, when not to use AI, "
              "AI instead of hiring, AI fitness assessment",
        "ru": "внедрение ИИ в бизнес, языковые модели в процессах, когда не нужен ИИ, "
              "ИИ вместо найма, оценка пригодности ИИ",
    },
    schema=schema_for("ai", TITLE, DESC),
    sections=[("service", "ai"), ("fragment", "contact-form")],
)
