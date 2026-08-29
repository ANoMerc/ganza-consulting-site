# -*- coding: utf-8 -*-
"""Главная. Витрина: кто мы, что делаем, что получилось, что пишем."""
PAGE = dict(
    slug="",
    order=0,
    nav_key="",
    title={
        "en": "Ganza Consulting — Business Consulting, Automation & AI",
        "ru": "Ganza Consulting — консалтинг, автоматизация и ИИ",
    },
    description={
        "en": "Independent consulting studio for the hard problems bigger firms pass on: "
              "consulting, process automation and AI, project management, web development.",
        "ru": "Независимый консалтинг для задач, за которые не берутся другие: автоматизация "
              "процессов и ИИ, проектный менеджмент, веб-разработка.",
    },
    keywords={
        "en": "business consulting, independent consultant, process automation, AI implementation, "
              "project management consulting, custom web development",
        "ru": "бизнес-консалтинг, независимый консультант, автоматизация бизнес-процессов, "
              "внедрение ИИ, проектный менеджмент, разработка сайтов на заказ",
    },
    sections=[
        ("fragment", "hero"),
        ("services_teaser", None),
        ("fragment", "builder-trigger"),
        ("cases", 3),
        ("posts", 3),
        ("fragment", "about"),
        ("fragment", "contact-form"),
    ],
)
