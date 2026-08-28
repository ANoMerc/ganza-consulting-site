#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared building blocks for build_site.py and build_blog.py.

Everything that both the landing page and the blog need — <head> assembly,
the ticker/header/footer chrome, JSON-LD helpers, analytics snippet — lives
here so the two generators can never drift apart.
"""
import html as html_mod
import json
import math
import os
import re

esc = html_mod.escape

# ---------------------------------------------------------------------------
# GLOBAL CONFIG — change the domain here and everything regenerates.
# ---------------------------------------------------------------------------
SITE = "https://anomerc.github.io/ganza-consulting-site"
ROOT = os.path.dirname(os.path.abspath(__file__))

BRAND = "Ganza Consulting"
TELEGRAM = "https://t.me/groovebliss"
LINKEDIN = "https://www.linkedin.com/in/george-mercer-55520b388/"
EMAIL = "onegeorgemercer@gmail.com"

AUTHOR_NAME = "George Mercer"
AUTHOR_BIO = {
    "en": "Independent consultant and founder of Ganza Consulting. Works on the single hard "
          "problems other firms decline: non-standard automation, stalled projects, messy "
          "processes and custom web builds. Every article here is written from engagements "
          "that were actually delivered — not from a content calendar.",
    "ru": "Независимый консультант и основатель Ganza Consulting. Берёт единичные сложные "
          "задачи, от которых отказываются другие: нетиповую автоматизацию, застрявшие "
          "проекты, запутанные процессы и нестандартную веб-разработку. Каждая статья здесь "
          "написана по реально сделанным проектам, а не по контент-плану.",
}

# Words per minute used for the honest "N min read" figure.
WPM = {"en": 200, "ru": 180}

LABELS = {
    "en": {
        "nav_services": "Services", "nav_cases": "Cases", "nav_pricing": "Pricing",
        "nav_about": "About", "nav_blog": "Blog", "nav_contact": "Contact",
        "menu": "MENU", "telegram": "TELEGRAM ↗",
        "home": "Home", "blog": "Blog",
        "min_read": "min read", "updated": "Updated",
        "contents": "CONTENTS", "takeaways": "WHAT TO TAKE AWAY",
        "faq": "FREQUENTLY ASKED QUESTIONS", "author": "ABOUT THE AUTHOR",
        "related": "RELATED READING", "all_articles": "← ALL ARTICLES",
        "prev": "← PREVIOUS", "next": "NEXT →",
        "cta_text": "Have a problem like this one? We take on the single hard cases other consultants pass on — fixed scope, a written answer, and a number you can act on.",
        "cta_tg": "MESSAGE ON TELEGRAM →", "cta_pricing": "SEE PRICING",
        "footer_h": "READY TO SORT<br>OUT THE CHAOS?<br>WRITE TO US.",
        "footer_joke": "COPYRIGHT IS BORING",
        "footer_legal": "© 2026 GANZA CONSULTING. ALL RIGHTS... WHATEVER.",
        "ticker": "NOW BOOKING Q4 2026&nbsp;&nbsp;—&nbsp;&nbsp;CONSULTING + AUTOMATION + PROJECT MANAGEMENT&nbsp;&nbsp;—&nbsp;&nbsp;NO TEMPLATES&nbsp;&nbsp;—&nbsp;&nbsp;",
        "filter_all": "ALL",
        "reading_now": "READING TIME",
    },
    "ru": {
        "nav_services": "Услуги", "nav_cases": "Кейсы", "nav_pricing": "Цены",
        "nav_about": "О нас", "nav_blog": "Блог", "nav_contact": "Контакты",
        "menu": "МЕНЮ", "telegram": "TELEGRAM ↗",
        "home": "Главная", "blog": "Блог",
        "min_read": "мин чтения", "updated": "Обновлено",
        "contents": "СОДЕРЖАНИЕ", "takeaways": "ЧТО ЗАБРАТЬ С СОБОЙ",
        "faq": "ЧАСТЫЕ ВОПРОСЫ", "author": "ОБ АВТОРЕ",
        "related": "ПО ТЕМЕ", "all_articles": "← ВСЕ СТАТЬИ",
        "prev": "← ПРЕДЫДУЩАЯ", "next": "СЛЕДУЮЩАЯ →",
        "cta_text": "Похожая задача? Мы берём единичные сложные случаи, за которые не берутся другие: фиксированный объём, письменный ответ и цифра, с которой можно работать.",
        "cta_tg": "НАПИСАТЬ В TELEGRAM →", "cta_pricing": "СМОТРЕТЬ ЦЕНЫ",
        "footer_h": "ПОРА РАЗГРЕСТИ<br>ХАОС?<br>НАПИШИТЕ НАМ.",
        "footer_joke": "КОПИРАЙТ — СКУКА",
        "footer_legal": "© 2026 GANZA CONSULTING. ВСЕ ПРАВА... НЕВАЖНО.",
        "ticker": "ПРИНИМАЕМ ПРОЕКТЫ НА Q4 2026&nbsp;&nbsp;—&nbsp;&nbsp;КОНСАЛТИНГ + АВТОМАТИЗАЦИЯ + ПРОЕКТНЫЙ МЕНЕДЖМЕНТ&nbsp;&nbsp;—&nbsp;&nbsp;БЕЗ ШАБЛОНОВ&nbsp;&nbsp;—&nbsp;&nbsp;",
        "filter_all": "ВСЕ",
        "reading_now": "ВРЕМЯ ЧТЕНИЯ",
    },
}

MONTHS = {
    "en": ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"],
    "ru": ["января", "февраля", "марта", "апреля", "мая", "июня", "июля",
           "августа", "сентября", "октября", "ноября", "декабря"],
}


def fmt_date(iso, lang):
    y, m, d = iso.split("-")
    if lang == "ru":
        return f"{int(d)} {MONTHS['ru'][int(m) - 1]} {y}"
    return f"{MONTHS['en'][int(m) - 1]} {int(d)}, {y}"


def strip_tags(s):
    return re.sub(r"<[^>]+>", " ", s)


def count_words(s):
    return len(re.findall(r"[\w'’-]+", strip_tags(s), flags=re.UNICODE))


# ---------------------------------------------------------------------------
# HEAD
# ---------------------------------------------------------------------------
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
           "%3Crect width='100' height='100' fill='%230d0d0a'/%3E%3Ctext x='50' y='72' font-size='68' "
           "font-family='Arial Black,sans-serif' font-weight='900' fill='%23e8ff2e' text-anchor='middle'"
           "%3EG%3C/text%3E%3C/svg%3E")

FONTS = ("https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Mono:wght@400;700"
         "&family=Inter:wght@400;500;600;700&display=swap")


def build_head(*, lang, title, description, keywords, canonical, alt_urls, og_image,
               og_image_alt, og_type, p, jsonld, extra_meta="", robots=None, css=("style", "builder"),
               feed=None):
    """Assemble a complete <head>. `alt_urls` maps lang code -> absolute URL."""
    robots = robots or "index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1"
    alts = "\n".join(
        f'<link rel="alternate" hreflang="{code}" href="{url}">' for code, url in alt_urls.items()
    )
    xdefault = alt_urls.get("en", canonical)
    css_links = "\n".join(f'<link rel="stylesheet" href="{p}css/{name}.css">' for name in css)
    feed_link = (f'\n<link rel="alternate" type="application/rss+xml" title="{esc(BRAND)} — {LABELS[lang]["blog"]}" href="{feed}">'
                 if feed else "")
    locale = "en_US" if lang == "en" else "ru_RU"
    alt_locale = "ru_RU" if lang == "en" else "en_US"
    return f"""<!DOCTYPE html>
<html lang="{lang}" data-lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{keywords}">
<meta name="author" content="{esc(AUTHOR_NAME)}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0d0d0a">
<link rel="canonical" href="{canonical}">
{alts}
<link rel="alternate" hreflang="x-default" href="{xdefault}">{feed_link}

<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(BRAND)}">
<meta property="og:locale" content="{locale}">
<meta property="og:locale:alternate" content="{alt_locale}">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_image_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">
{extra_meta}
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
{css_links}
{jsonld}<script src="{p}js/analytics.js" defer></script>
</head>
"""


# ---------------------------------------------------------------------------
# JSON-LD building blocks
# ---------------------------------------------------------------------------
def org_node():
    return {
        "@type": "Organization",
        "@id": f"{SITE}/#organization",
        "name": BRAND,
        "url": f"{SITE}/",
        "email": EMAIL,
        "logo": {"@type": "ImageObject", "url": f"{SITE}/img/og-cover.png",
                 "width": 1200, "height": 630},
        "sameAs": [TELEGRAM, LINKEDIN],
    }


def person_node(lang):
    return {
        "@type": "Person",
        "@id": f"{SITE}/#george-mercer",
        "name": AUTHOR_NAME,
        "url": f"{SITE}/#about" if lang == "en" else f"{SITE}/ru/#about",
        "image": f"{SITE}/img/founder.png",
        "description": AUTHOR_BIO[lang],
        "jobTitle": "Independent consultant" if lang == "en" else "Независимый консультант",
        "worksFor": {"@id": f"{SITE}/#organization"},
        "sameAs": [TELEGRAM, LINKEDIN],
        "knowsAbout": (
            ["Business consulting", "Process automation", "Artificial intelligence",
             "Project management", "Web development", "Digital transformation"]
            if lang == "en" else
            ["Бизнес-консалтинг", "Автоматизация процессов", "Искусственный интеллект",
             "Проектный менеджмент", "Веб-разработка", "Цифровая трансформация"]
        ),
    }


def jsonld_block(graph):
    payload = {"@context": "https://schema.org", "@graph": graph}
    return ('<script type="application/ld+json">\n'
            + json.dumps(payload, ensure_ascii=False, indent=2)
            + "\n</script>\n")


# ---------------------------------------------------------------------------
# CHROME: ticker / header / footer
# ---------------------------------------------------------------------------
def ticker(lang):
    text = LABELS[lang]["ticker"] * 2
    return f"""<div class="ticker" aria-hidden="true">
  <div class="ticker__track"><span>{text}</span></div>
</div>
"""


def header(lang, p, home, blog_href, alt_url, active=""):
    """Header for single-language pages (blog). `home` is the language home URL."""
    L = LABELS[lang]
    other = "ru" if lang == "en" else "en"
    ru_cls = "lang-switch__opt is-active" if lang == "ru" else "lang-switch__opt"
    en_cls = "lang-switch__opt is-active" if lang == "en" else "lang-switch__opt"
    return f"""<header class="site-header" id="top">
  <div class="site-header__inner">
    <a href="{home}" class="logo" data-track="logo">
      <span class="logo__mark">G</span>
      <span class="logo__text">GANZA<br>CONSULTING</span>
    </a>

    <nav class="nav" id="nav" aria-label="Main navigation">
      <a href="{home}#services">{L['nav_services']}</a>
      <a href="{home}#cases">{L['nav_cases']}</a>
      <a href="{home}#pricing">{L['nav_pricing']}</a>
      <a href="{blog_href}"{' class="is-active"' if active == "blog" else ''}>{L['nav_blog']}</a>
      <a href="{home}#contact">{L['nav_contact']}</a>
    </nav>

    <div class="header-actions">
      <a class="lang-switch" href="{alt_url}" hreflang="{other}" aria-label="Switch language" data-track="lang-switch">
        <span class="{ru_cls}">RU</span>
        <span class="lang-switch__sep">/</span>
        <span class="{en_cls}">EN</span>
      </a>
      <a class="btn btn--small btn--yellow" href="{TELEGRAM}" target="_blank" rel="noopener" data-track="header-telegram">{L['telegram']}</a>
      <button class="burger" id="burger" aria-label="Menu" type="button">{L['menu']}</button>
    </div>
  </div>
</header>
"""


def footer(lang, p):
    L = LABELS[lang]
    return f"""
<footer class="footer" id="contact">
  <div class="footer__top">
    <h2>{L['footer_h']}</h2>
    <div class="footer__contacts">
      <a class="contact-link" href="{TELEGRAM}" target="_blank" rel="noopener" data-track="footer-telegram">
        <span class="contact-link__label">TELEGRAM</span>
        <span class="contact-link__value">@groovebliss ↗</span>
      </a>
      <a class="contact-link" href="{LINKEDIN}" target="_blank" rel="noopener" data-track="footer-linkedin">
        <span class="contact-link__label">LINKEDIN</span>
        <span class="contact-link__value">george-mercer ↗</span>
      </a>
      <a class="contact-link" href="mailto:{EMAIL}" data-track="footer-email">
        <span class="contact-link__label">EMAIL</span>
        <span class="contact-link__value">{EMAIL} ↗</span>
      </a>
    </div>
  </div>

  <div class="footer__bottom">
    <p class="footer__joke">{L['footer_joke']}</p>
    <p class="footer__legal">{L['footer_legal']}</p>
  </div>
</footer>

<script src="{p}js/script.js"></script>
</body>
</html>
"""


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return full
