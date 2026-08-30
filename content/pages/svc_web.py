# -*- coding: utf-8 -*-
"""Направление: сайты и веб. Данные — в content/services/web.py."""
from core.services import schema_for

TITLE = {"en": "Websites that convert", "ru": "Сайты, которые работают"}
DESC = {
    "en": "Sites built around one target action, with language versions separated by meaning rather than dictionary, and sources you can edit without a contractor.",
    "ru": "Сайты вокруг одного целевого действия, с языковыми версиями, разведёнными по смыслу, и исходниками, которые вы правите без подрядчика.",
}

PAGE = dict(
    slug="services/web/",
    order=24,
    nav_key="services",
    builder=False,
    title={
        "en": "Websites That Convert — Ganza Consulting",
        "ru": "Сайты, которые работают — Ganza Consulting",
    },
    description={
        "en": "Built around one target action, in several languages that differ by meaning and not by dictionary, with sources and accesses that stay yours.",
        "ru": "Сайт вокруг одного целевого действия, на нескольких языках, разведённых по смыслу, с исходниками и доступами, которые остаются у вас.",
    },
    hero={
        "eyebrow": {"en": "SERVICES · WEB", "ru": "УСЛУГИ · САЙТЫ"},
        "h1": {"en": "WEBSITES THAT WORK", "ru": "САЙТЫ, КОТОРЫЕ РАБОТАЮТ"},
        "lead": {
            "en": "Traffic without enquiries is not a design problem. It is a problem of not knowing at which step the visitor stopped understanding, believing or finding.",
            "ru": "Трафик без заявок — не проблема дизайна. Это незнание того, на каком шаге посетитель перестал понимать, верить или находить.",
        },
    },
    keywords={
        "en": "multilingual website development, website conversion audit, custom website "
              "without CMS lock-in, bilingual site RU EN, landing page that converts",
        "ru": "разработка многоязычного сайта, аудит конверсии сайта, сайт без привязки к "
              "платформе, двуязычный сайт русский английский, сайт под заявки",
    },
    schema=schema_for("web", TITLE, DESC),
    sections=[("service", "web"), ("fragment", "contact-form")],
)
