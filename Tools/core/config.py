# -*- coding: utf-8 -*-
"""ЯДРО · Настройки.

Всё, что меняется реже всего и при этом влияет на весь сайт. Меняешь домен
здесь — обновляются canonical, hreflang, JSON-LD, sitemap и RSS во всех
шестидесяти файлах.
"""
import os

# --- где живёт сайт --------------------------------------------------------
SITE = "https://anomerc.github.io/ganza-consulting-site"

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONTENT = os.path.join(ROOT, "content")
ASSETS = "assets"           # относительный путь к css/js/img от корня сайта

# --- кто --------------------------------------------------------------------
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

# --- языки ------------------------------------------------------------------
# Основной рынок — русскоязычный, поэтому русская версия лежит в корне.
# Английская — для тех, кто по-русски не читает. Поменять местами: три
# строки ниже плюс LEGACY_PREFIXES, редиректы со старых адресов сборка
# сделает сама.
LANGS = ("ru", "en")
DEFAULT_LANG = "ru"                        # сюда указывает x-default
LANG_PREFIX = {"ru": "", "en": "en/"}      # ru в корне, en в подпапке

# Адреса, по которым сайт жил раньше. Сборка кладёт по ним редиректы, чтобы
# старые ссылки и то, что уже попало в индекс, не превращалось в 404.
# Ключ — старый префикс, значение — новый.
LEGACY_PREFIXES = {"ru/": ""}

WPM = {"en": 200, "ru": 180}              # слов в минуту для времени чтения

# --- прайсинг (дублируется в JSON-LD, поэтому живёт здесь) ------------------
OFFERS = [
    dict(price="2500", key="flagship",
         name={"en": "The Problem Everyone Else Turned Down",
               "ru": "Задача, от которой отказались другие"},
         desc={"en": "Flagship engagement for a single non-standard problem. Usually 2–6 weeks.",
               "ru": "Флагманский формат под одну нетиповую задачу. Обычно 2–6 недель."}),
    dict(price="450", key="pinpoint",
         name={"en": "Pinpoint Expertise", "ru": "Точечная экспертиза"},
         desc={"en": "One focused question answered in writing. 3–5 days.",
               "ru": "Один сфокусированный вопрос с письменным ответом. 3–5 дней."}),
    dict(price="1100", key="fast",
         name={"en": "Fast Implementation of a Single Solution",
               "ru": "Быстрое внедрение точечного решения"},
         desc={"en": "Build and ship one specific solution. 1–3 weeks.",
               "ru": "Собрать и внедрить одно конкретное решение. 1–3 недели."}),
    dict(price="1400", key="reserve",
         name={"en": "Expert Reserve", "ru": "Экспертный резерв"},
         desc={"en": "Monthly access to an expert on call for ongoing hard questions.",
               "ru": "Ежемесячный доступ к эксперту под текущие сложные вопросы."}),
]

# --- подписи интерфейса -----------------------------------------------------
LABELS = {
    "en": {
        "home": "Home", "blog": "Blog", "cases": "Cases", "services": "Services",
        "contact": "Contact", "menu": "MENU", "telegram": "TELEGRAM ↗",
        "min_read": "min read", "updated": "Updated",
        "contents": "CONTENTS", "takeaways": "WHAT TO TAKE AWAY",
        "faq": "FREQUENTLY ASKED QUESTIONS", "author": "ABOUT THE AUTHOR",
        "related": "RELATED READING", "prev": "← PREVIOUS", "next": "NEXT →",
        "read_article": "READ THE ARTICLE →", "all_cases": "ALL CASES →",
        "all_posts": "ALL ARTICLES →", "filter_all": "ALL",
        "share": "SHARE", "top": "↑ TOP", "problem": "Problem",
        "did": "What we did", "result": "Result",
        "cta_text": "Have a problem like this one? We take on the single hard cases other "
                    "consultants pass on — fixed scope, a written answer, and a number you can act on.",
        "cta_tg": "MESSAGE ON TELEGRAM →", "cta_pricing": "SEE PRICING",
        "footer_h": "READY TO SORT<br>OUT THE CHAOS?<br>WRITE TO US.",
        "footer_joke": "COPYRIGHT IS BORING",
        "footer_legal": "© 2026 GANZA CONSULTING. ALL RIGHTS... WHATEVER.",
        "ticker": "NOW BOOKING Q4 2026&nbsp;&nbsp;—&nbsp;&nbsp;CONSULTING + AUTOMATION + "
                  "PROJECT MANAGEMENT&nbsp;&nbsp;—&nbsp;&nbsp;NO TEMPLATES&nbsp;&nbsp;—&nbsp;&nbsp;",
    },
    "ru": {
        "home": "Главная", "blog": "Блог", "cases": "Кейсы", "services": "Услуги",
        "contact": "Контакты", "menu": "МЕНЮ", "telegram": "TELEGRAM ↗",
        "min_read": "мин чтения", "updated": "Обновлено",
        "contents": "СОДЕРЖАНИЕ", "takeaways": "ЧТО ЗАБРАТЬ С СОБОЙ",
        "faq": "ЧАСТЫЕ ВОПРОСЫ", "author": "ОБ АВТОРЕ",
        "related": "ПО ТЕМЕ", "prev": "← ПРЕДЫДУЩАЯ", "next": "СЛЕДУЮЩАЯ →",
        "read_article": "ЧИТАТЬ СТАТЬЮ →", "all_cases": "ВСЕ КЕЙСЫ →",
        "all_posts": "ВСЕ СТАТЬИ →", "filter_all": "ВСЕ",
        "share": "ПОДЕЛИТЬСЯ", "top": "↑ НАВЕРХ", "problem": "Проблема",
        "did": "Что сделали", "result": "Результат",
        "cta_text": "Похожая задача? Мы берём единичные сложные случаи, за которые не берутся "
                    "другие: фиксированный объём, письменный ответ и цифра, с которой можно работать.",
        "cta_tg": "НАПИСАТЬ В TELEGRAM →", "cta_pricing": "СМОТРЕТЬ ЦЕНЫ",
        "footer_h": "ПОРА РАЗГРЕСТИ<br>ХАОС?<br>НАПИШИТЕ НАМ.",
        "footer_joke": "КОПИРАЙТ — СКУКА",
        "footer_legal": "© 2026 GANZA CONSULTING. ВСЕ ПРАВА... НЕВАЖНО.",
        "ticker": "ПРИНИМАЕМ ПРОЕКТЫ НА Q4 2026&nbsp;&nbsp;—&nbsp;&nbsp;КОНСАЛТИНГ + АВТОМАТИЗАЦИЯ + "
                  "ПРОЕКТНЫЙ МЕНЕДЖМЕНТ&nbsp;&nbsp;—&nbsp;&nbsp;БЕЗ ШАБЛОНОВ&nbsp;&nbsp;—&nbsp;&nbsp;",
    },
}

MONTHS = {
    "en": ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"],
    "ru": ["января", "февраля", "марта", "апреля", "мая", "июня", "июля",
           "августа", "сентября", "октября", "ноября", "декабря"],
}

# --- меню -------------------------------------------------------------------
# Порядок пунктов в шапке. Ключ 'page' — slug страницы, 'anchor' — якорь на ней.
NAV = [
    dict(key="services", page="services"),
    dict(key="cases", page="cases"),
    dict(key="blog", page="blog"),
    dict(key="contact", page="", anchor="contact"),
]
