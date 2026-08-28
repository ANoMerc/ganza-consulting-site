# -*- coding: utf-8 -*-
"""Кейсы. Карточки собираются из content/cases/*.py — добавляются скриптом."""
PAGE = dict(
    slug="cases/",
    order=2,
    nav_key="cases",
    builder=False,
    title={
        "en": "Cases — what we actually delivered | Ganza Consulting",
        "ru": "Кейсы — что реально сделано | Ganza Consulting",
    },
    description={
        "en": "Anonymised breakdowns of delivered work: the problem, what we did and the "
              "number that moved. Retail analytics, automation instead of a hire, web builds.",
        "ru": "Обезличенные разборы сделанной работы: задача, что сделали и какая цифра "
              "изменилась. Аналитика в ритейле, автоматизация вместо найма, сайты на 5 языков.",
    },
    hero={
        "eyebrow": {"en": "CASES", "ru": "КЕЙСЫ"},
        "h1": {"en": "WHAT WE ACTUALLY DELIVERED", "ru": "ЧТО РЕАЛЬНО СДЕЛАНО"},
        "lead": {
            "en": "Clients are anonymised, the numbers are not. Each case says what was wrong, "
                  "what we did about it, and which figure moved.",
            "ru": "Клиенты обезличены, цифры — нет. В каждом кейсе: что было не так, что "
                  "сделали и какая цифра сдвинулась.",
        },
    },
    keywords={
        "en": "consulting case studies, automation case study, retail analytics case, "
              "multilingual website case",
        "ru": "кейсы консалтинга, кейс автоматизации, аналитика в ритейле кейс, "
              "мультиязычный сайт кейс",
    },
    sections=[("cases", None)],
)
