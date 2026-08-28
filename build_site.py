#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates the landing page in both languages from _src/index.master.html.

    /index.html      — English (default language of the site, x-default)
    /ru/index.html   — Russian
    /en/index.html   — canonical redirect to /, so old EN links keep working

The master file holds BOTH languages inline (.lang-en / .lang-ru spans, hidden
by CSS). Each generated file differs only in <head>, the <html data-lang> value
and relative asset paths — so search engines get two indexable pages while the
RU/EN button still switches instantly with no reload.

Run:  python3 build_site.py
"""
import os
import re

from buildlib import (SITE, BRAND, EMAIL, TELEGRAM, LINKEDIN, AUTHOR_NAME, LABELS,
                      build_head, jsonld_block, org_node, person_node, esc, write, ROOT)

MASTER = os.path.join(ROOT, "_src", "index.master.html")

META = {
    "en": dict(
        title="Ganza Consulting — Business Consulting, Automation &amp; AI",
        description="Independent consulting studio for the hard problems bigger firms pass on: consulting, process automation and AI, project management, web development.",
        keywords="business consulting, independent consultant, boutique consulting studio, business process automation, AI implementation, project management consulting, custom web development, digital transformation consulting, operations consulting, consulting for startups",
        og_alt="Ganza Consulting — independent consulting, automation and project management",
    ),
    "ru": dict(
        title="Ganza Consulting — консалтинг, автоматизация и ИИ",
        description="Независимый консалтинг для задач, за которые не берутся другие: автоматизация процессов и ИИ, проектный менеджмент, веб-разработка.",
        keywords="бизнес-консалтинг, независимый консультант, автоматизация бизнес-процессов, внедрение ИИ, проектный менеджмент, разработка сайтов на заказ, цифровая трансформация, консалтинг для стартапов, аудит бизнес-процессов, управление проектами",
        og_alt="Ganza Consulting — независимый консалтинг, автоматизация и проектный менеджмент",
    ),
}

URLS = {"en": f"{SITE}/", "ru": f"{SITE}/ru/"}

OFFERS = [
    dict(en_name="The Problem Everyone Else Turned Down", ru_name="Задача, от которой отказались другие",
         price="2500", en_desc="Flagship engagement for a single non-standard problem. Individual estimate, usually 2–6 weeks.",
         ru_desc="Флагманский формат под одну нетиповую задачу. Индивидуальный расчёт, обычно 2–6 недель."),
    dict(en_name="Pinpoint Expertise", ru_name="Точечная экспертиза", price="450",
         en_desc="One focused question answered in writing. 3–5 days.",
         ru_desc="Один сфокусированный вопрос с письменным ответом. 3–5 дней."),
    dict(en_name="Fast Implementation of a Single Solution", ru_name="Быстрое внедрение точечного решения",
         price="1100", en_desc="Build and ship one specific solution. 1–3 weeks.",
         ru_desc="Собрать и внедрить одно конкретное решение. 1–3 недели."),
    dict(en_name="Expert Reserve", ru_name="Экспертный резерв", price="1400",
         en_desc="Monthly access to an expert on call for ongoing hard questions.",
         ru_desc="Ежемесячный доступ к эксперту под текущие сложные вопросы."),
]


# ---------------------------------------------------------------------------
# FAQ extraction — the FAQPage schema is generated from the real page markup,
# so it can never fall out of sync with what a visitor actually reads.
# ---------------------------------------------------------------------------
def extract_faq(master, lang):
    other = "ru" if lang == "en" else "en"
    items = []
    for block in re.findall(r'<details class="faq-item">(.*?)</details>', master, re.S):
        summary = re.search(r"<summary>(.*?)</summary>", block, re.S)
        answer = re.search(r"<p>(.*?)</p>", block, re.S)
        if not (summary and answer):
            continue

        def pick(chunk):
            m = re.search(rf'<span class="lang-{lang}">(.*?)</span>', chunk, re.S)
            return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""

        q, a = pick(summary.group(1)), pick(answer.group(1))
        if q and a:
            items.append((q.strip("«»\"“” "), a))
    return items


def faq_node(items, lang):
    return {
        "@type": "FAQPage",
        "@id": f"{URLS[lang]}#faq",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }


def service_node(lang):
    return {
        "@type": "ProfessionalService",
        "@id": f"{SITE}/#service",
        "name": BRAND,
        "url": URLS[lang],
        "image": f"{SITE}/img/og-cover.png",
        "email": EMAIL,
        "founder": {"@id": f"{SITE}/#george-mercer"},
        "parentOrganization": {"@id": f"{SITE}/#organization"},
        "description": META[lang]["description"],
        "areaServed": "Worldwide" if lang == "en" else "Весь мир",
        "availableLanguage": ["en", "ru"],
        "priceRange": "$450–$2500+",
        "sameAs": [TELEGRAM, LINKEDIN],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Engagement formats" if lang == "en" else "Форматы работы",
            "itemListElement": [
                {
                    "@type": "Offer",
                    "priceCurrency": "USD",
                    "price": o["price"],
                    "itemOffered": {
                        "@type": "Service",
                        "name": o[f"{lang}_name"],
                        "description": o[f"{lang}_desc"],
                    },
                }
                for o in OFFERS
            ],
        },
    }


def website_node(lang):
    return {
        "@type": "WebSite",
        "@id": f"{SITE}/#website",
        "url": f"{SITE}/",
        "name": BRAND,
        "inLanguage": lang,
        "publisher": {"@id": f"{SITE}/#organization"},
    }


def build_lang(master, lang):
    p = "" if lang == "en" else "../"
    url_en = "./" if lang == "en" else "../"
    url_ru = "ru/" if lang == "en" else "./"

    body = (master
            .replace("{{P}}", p)
            .replace("{{BLOG}}", "blog/")
            .replace("{{URLEN}}", url_en)
            .replace("{{URLRU}}", url_ru))

    graph = [
        org_node(),
        website_node(lang),
        person_node(lang),
        service_node(lang),
        faq_node(extract_faq(master, lang), lang),
    ]

    head = build_head(
        lang=lang,
        title=META[lang]["title"],
        description=esc(META[lang]["description"]),
        keywords=esc(META[lang]["keywords"]),
        canonical=URLS[lang],
        alt_urls={"en": URLS["en"], "ru": URLS["ru"]},
        og_image=f"{SITE}/img/og-cover.png",
        og_image_alt=esc(META[lang]["og_alt"]),
        og_type="website",
        p=p,
        jsonld=jsonld_block(graph),
        css=("style", "builder", "glass"),
        feed=f"{SITE}/blog/feed.xml" if lang == "en" else f"{SITE}/ru/blog/feed.xml",
    )

    html = head + '<body class="page-home">\n' + body + f"""

<script src="{p}js/script.js"></script>
<script src="{p}js/builder.js"></script>
</body>
</html>
"""
    out = "index.html" if lang == "en" else "ru/index.html"
    write(out, html)
    print(f"wrote {out} ({lang}, {len(html) // 1024} KB)")


REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Ganza Consulting</title>
<link rel="canonical" href="{site}/">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url={site}/">
<script>location.replace("{site}/");</script>
</head>
<body>
<p>The English site has moved to <a href="{site}/">{site}/</a>.</p>
</body>
</html>
"""


def main():
    master = open(MASTER, encoding="utf-8").read()
    build_lang(master, "en")
    build_lang(master, "ru")
    write("en/index.html", REDIRECT.format(site=SITE))
    print("wrote en/index.html (redirect → /)")


if __name__ == "__main__":
    main()
