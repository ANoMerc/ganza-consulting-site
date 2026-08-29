# -*- coding: utf-8 -*-
"""Услуги: как мы работаем, что делаем, сколько стоит, частые возражения."""
from core import config as cfg
from core.pages import crumbs, faq_nodes


def schema(ctx):
    """ProfessionalService с прайсингом, хлебные крошки и FAQ этой же страницы.

    FAQPage считается из content/fragments/faq.html — вопросы и разметка не
    могут разойтись, потому что источник один.
    """
    return crumbs(ctx, (ctx.L["services"], "services/")) + faq_nodes(ctx) + [{
        "@type": "ProfessionalService",
        "@id": f"{cfg.SITE}/#service",
        "name": cfg.BRAND,
        "url": ctx.abs(),
        "email": cfg.EMAIL,
        "founder": {"@id": f"{cfg.SITE}/#george-mercer"},
        "areaServed": "Worldwide" if ctx.lang == "en" else "Весь мир",
        "availableLanguage": list(cfg.LANGS),
        "priceRange": "$450–$2500+",
        "sameAs": [cfg.TELEGRAM, cfg.LINKEDIN],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Engagement formats" if ctx.lang == "en" else "Форматы работы",
            "itemListElement": [
                {"@type": "Offer", "priceCurrency": "USD", "price": o["price"],
                 "itemOffered": {"@type": "Service", "name": o["name"][ctx.lang],
                                 "description": o["desc"][ctx.lang]}}
                for o in cfg.OFFERS
            ],
        },
    }]


PAGE = dict(
    slug="services/",
    order=1,
    nav_key="services",
    title={
        "en": "Services & Pricing — Ganza Consulting",
        "ru": "Услуги и цены — Ganza Consulting",
    },
    description={
        "en": "How we work in four steps, the four kinds of problem we take on, what each "
              "format costs and why, and honest answers to the objections raised before signing.",
        "ru": "Как мы работаем за четыре шага, какие задачи берём, сколько стоит каждый формат "
              "и почему, и честные ответы на возражения до подписания.",
    },
    hero={
        "eyebrow": {"en": "SERVICES & PRICING", "ru": "УСЛУГИ И ЦЕНЫ"},
        "h1": {"en": "WHAT I DO AND WHAT IT COSTS",
               "ru": "ЧТО Я ДЕЛАЮ И СКОЛЬКО ЭТО СТОИТ"},
        "lead": {
            "en": "Four engagement formats instead of a funnel of identical packages. Each one "
                  "states what's included, what it costs and how long it takes — before the first call.",
            "ru": "Четыре формата работы вместо воронки одинаковых пакетов. У каждого "
                  "написано, что входит, сколько стоит и сколько занимает — до первого "
                  "разговора, а не после него.",
        },
    },
    keywords={
        "en": "consulting services, consulting pricing, business process automation cost, "
              "project management services, custom web development pricing",
        "ru": "услуги консалтинга, стоимость консалтинга, цена автоматизации бизнес-процессов, "
              "управление проектами услуги, разработка сайтов цена",
    },
    schema=schema,
    sections=[
        ("fragment", "how-we-work"),
        ("fragment", "services"),
        ("fragment", "builder-trigger"),
        ("fragment", "pricing"),
        ("fragment", "faq"),
        ("fragment", "contact-form"),
    ],
)
