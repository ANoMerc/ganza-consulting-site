# -*- coding: utf-8 -*-
"""ЯДРО · Настройки.

Всё, что меняется реже всего и при этом влияет на весь сайт. Меняешь домен
здесь — обновляются canonical, hreflang, JSON-LD, sitemap и RSS во всех
шестидесяти файлах.
"""
import datetime
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

# Куда форма шлёт заявку — Supabase Edge Function submit-lead.
# Пусто = форма собирается, но не отправляет; заполнить после деплоя функции:
#   https://<project-ref>.supabase.co/functions/v1/submit-lead
FORM_ENDPOINT = ""
AUTHOR_NAME = "George Mercer"

# --- контролёр данных (для политики конфиденциальности) ----------------------
# ЗАПОЛНИТЬ перед публикацией. По грузинскому закону уведомление должно
# называть, кто именно обрабатывает данные, и давать рабочий контакт.
# Если решите не публиковать идентификационный номер — оставьте пустым,
# строка не появится, но юриста об этом стоит спросить.
CONTROLLER = {
    "legal_name": {"en": "Individual entrepreneur George Mercer",
                   "ru": "Индивидуальный предприниматель George Mercer"},
    "reg_number": "",                       # идентификационный номер ИП, если публикуем
    "country":    {"en": "Georgia", "ru": "Грузия"},
    "address":    "",                       # адрес регистрации, если публикуем
    "since":      "2024-03-01",             # дата вступления в силу закона Грузии
    "updated":    "2026-08-29",             # дата редакции политики
}

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
         name={"en": "Where the Checklist Runs Out",
               "ru": "Там, где чек-лист заканчивается"},
         desc={"en": "One problem that doesn't split into clear stages, so no ready-made "
                     "package fits it. Analysis, automation and development as the task "
                     "requires, from one person. Usually 2–6 weeks.",
               "ru": "Одна задача, которая не разбивается на понятные этапы, поэтому под "
                     "неё не подходит ни один готовый пакет. Аналитика, автоматизация и "
                     "разработка в нужной пропорции, от одного человека. Обычно 2–6 недель."}),
    dict(price="450", key="pinpoint",
         name={"en": "Pinpoint Expertise", "ru": "Точечная экспертиза"},
         desc={"en": "One question, taken apart properly and answered in writing, with "
                     "the arithmetic shown. No implementation. 3–5 days.",
               "ru": "Один вопрос, разобранный до конца и отвеченный письменно, с "
                     "показанным расчётом. Без внедрения. 3–5 дней."}),
    dict(price="1100", key="fast",
         name={"en": "Fast Implementation of a Single Solution",
               "ru": "Быстрое внедрение точечного решения"},
         desc={"en": "You already know what is needed. I design it, build it, test it and "
                     "hand over documentation plus two weeks of support. 1–3 weeks.",
               "ru": "Вы уже знаете, что нужно. Проектирую, собираю, тестирую и отдаю с "
                     "документацией и двумя неделями поддержки. 1–3 недели."}),
    dict(price="600", key="reserve",
         name={"en": "Expert Reserve", "ru": "Экспертный резерв"},
         desc={"en": "A fixed pool of hours each month for questions as they come up. "
                     "You are buying availability, not activity — nothing is billed for "
                     "simply existing.",
               "ru": "Оговорённый пул часов в месяц под вопросы по мере их появления. "
                     "Вы платите за доступность, а не за активность: за сам факт "
                     "существования подписки счёт не выставляется."}),
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
        "cta_text": "Have a problem like this one? I take on the work a checklist doesn't "
                    "close — fixed scope, a written answer, and a number you can act on. "
                    "The price is known before the work starts.",
        "cta_tg": "MESSAGE ON TELEGRAM →", "cta_pricing": "SEE PRICING",
        "footer_h": "READY TO SORT<br>OUT THE CHAOS?<br>WRITE TO US.",
        "privacy": "Privacy policy",
        "footer_joke": "COPYRIGHT IS BORING",
        "footer_legal": "© 2026 GANZA CONSULTING. ALL RIGHTS... WHATEVER.",
        "ticker": "NOW BOOKING {{QUARTER}}&nbsp;&nbsp;—&nbsp;&nbsp;CONSULTING + AUTOMATION + "
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
        "cta_text": "Похожая задача? Я берусь за то, что не закрывается чек-листом: "
                    "фиксированный объём, письменный ответ и цифра, с которой можно работать. "
                    "Цена известна до начала работы.",
        "cta_tg": "НАПИСАТЬ В TELEGRAM →", "cta_pricing": "СМОТРЕТЬ ЦЕНЫ",
        "footer_h": "ПОРА РАЗГРЕСТИ<br>ХАОС?<br>НАПИШИТЕ НАМ.",
        "privacy": "Политика конфиденциальности",
        "footer_joke": "КОПИРАЙТ — СКУКА",
        "footer_legal": "© 2026 GANZA CONSULTING. ВСЕ ПРАВА... НЕВАЖНО.",
        "ticker": "ПРИНИМАЕМ ПРОЕКТЫ НА {{QUARTER}}&nbsp;&nbsp;—&nbsp;&nbsp;КОНСАЛТИНГ + АВТОМАТИЗАЦИЯ + "
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


# --- квартал, на который открыт набор ---------------------------------------
# Считается от даты сборки: берём дату через месяц и её квартал. Так строка
# «принимаем проекты на ...» не устаревает молча — раньше там был хардкод.
def booking_quarter(today=None):
    """Следующий квартал относительно даты сборки.

    В конце августа 2026 набор идёт на Q4 2026, а не на текущий Q3 — поэтому
    берём квартал даты и сдвигаем на один вперёд.
    """
    d = today or datetime.date.today()
    q = (d.month - 1) // 3 + 1          # текущий квартал
    q, y = (q + 1, d.year) if q < 4 else (1, d.year + 1)
    return f"Q{q} {y}"
