# -*- coding: utf-8 -*-
"""ЯДРО · Страницы направлений.

Направление описывается данными в content/services/*.py, а не свёрсткой. Смысл
тот же, что у кейсов: пять страниц обязаны отвечать на одни и те же семь
вопросов, и структура это гарантирует, а проза — нет.

Семь блоков каждой страницы:
    for_whom   в какой ситуации это вам нужно
    steps      что происходит по шагам
    you_keep   что остаётся у вас после
    formats    какие форматы из прайса подходят
    case       кейс, если он есть
    reading    статьи по теме
    not_this   чего я в этом направлении не делаю
"""
from . import config as cfg
from .theme import esc


def _fmt(key, lang):
    for o in cfg.OFFERS:
        if o["key"] == key:
            return o
    raise KeyError(key)


def schema_for(slug, title, description):
    """Хлебные крошки + узел Service для страницы направления.

    Пять страниц описываются одинаково по построению, а не по внимательности:
    отдельная функция на страницу — это пять мест, где можно забыть узел.
    """
    def schema(ctx):
        from .pages import crumbs
        lang = ctx.lang
        return crumbs(ctx,
                      (ctx.L["services"], "services/"),
                      (title[lang], f"services/{slug}/")) + [{
            "@type": "Service",
            "@id": ctx.abs() + "#service",
            "name": title[lang],
            "description": description[lang],
            "url": ctx.abs(),
            "serviceType": title[lang],
            "provider": {"@id": f"{cfg.SITE}/#service"},
            "areaServed": "Worldwide" if lang == "en" else "Весь мир",
            "availableLanguage": list(cfg.LANGS),
            "inLanguage": lang,
        }]
    return schema


def render(svc, ctx):
    lang, L = ctx.lang, ctx.L
    T = {
        "ru": dict(for_whom="КОГДА ЭТО ВАМ НУЖНО", steps="КАК ИДЁТ РАБОТА",
                   keep="ЧТО ОСТАЁТСЯ У ВАС", formats="СКОЛЬКО СТОИТ",
                   case="КЕЙС ПО ЭТОМУ НАПРАВЛЕНИЮ", reading="ПОЧИТАТЬ ПО ТЕМЕ",
                   not_this="ЧЕГО Я ЗДЕСЬ НЕ ДЕЛАЮ", all_prices="ВСЕ ФОРМАТЫ И ЦЕНЫ →",
                   discuss="ОБСУДИТЬ ЗАДАЧУ →", take="За что я берусь и за что нет →"),
        "en": dict(for_whom="WHEN YOU NEED THIS", steps="HOW THE WORK RUNS",
                   keep="WHAT YOU KEEP", formats="WHAT IT COSTS",
                   case="A CASE FROM THIS AREA", reading="RELATED READING",
                   not_this="WHAT I DON'T DO HERE", all_prices="ALL FORMATS & PRICING →",
                   discuss="DISCUSS THE PROBLEM →", take="What I take on and what I decline →"),
    }[lang]

    def block(tag, title, inner, cls=""):
        return (f'<section class="svc-block {cls}" data-reveal>\n'
                f'  <h2 class="svc-block__title">{title}</h2>\n{inner}\n</section>\n')

    out = []

    out.append(block("for", T["for_whom"],
        '  <ul class="svc-list">' +
        "".join(f"<li>{esc(x[lang])}</li>" for x in svc["for_whom"]) + "</ul>"))

    lis = "".join(f'<li><strong>{esc(t[lang])}</strong><span>{esc(b[lang])}</span></li>'
                  for t, b in svc["steps"])
    out.append(block("steps", T["steps"], f'  <ol class="svc-steps">{lis}</ol>'))

    out.append(block("keep", T["keep"],
        '  <ul class="svc-list svc-list--check">' +
        "".join(f"<li>{esc(x[lang])}</li>" for x in svc["you_keep"]) + "</ul>"))

    cards = []
    for key, note in svc["formats"]:
        o = _fmt(key, lang)
        # Разряды: в русском — неразрывный пробел, в английском — запятая.
        price = f'${int(o["price"]):,}'
        if lang == "ru":
            price = price.replace(",", " ")
        per = "/мес" if o["key"] == "reserve" and lang == "ru" else ("/mo" if o["key"] == "reserve" else "")
        cards.append(
            f'    <a class="svc-price" href="{ctx.to("services/")}#pricing">\n'
            f'      <span class="svc-price__name">{esc(o["name"][lang])}</span>\n'
            f'      <span class="svc-price__note">{esc(note[lang])}</span>\n'
            f'      <span class="svc-price__num">{price}{per}</span>\n'
            f'    </a>')
    out.append(block("price", T["formats"],
        '  <div class="svc-prices">\n' + "\n".join(cards) + "\n  </div>\n"
        f'  <p class="svc-more"><a class="btn btn--outline" href="{ctx.to("services/")}#pricing">{T["all_prices"]}</a></p>'))

    if svc.get("case"):
        c = svc["case"]
        out.append(block("case", T["case"],
            f'  <a class="svc-case" href="{ctx.to(c["path"])}">\n'
            f'    <span class="svc-case__stat">{esc(c["stat"][lang])}</span>\n'
            f'    <span class="svc-case__title">{esc(c["title"][lang])}</span>\n'
            f'    <span class="svc-case__lead">{esc(c["lead"][lang])}</span>\n'
            f'  </a>'))

    links = "".join(
        f'<li><a href="{ctx.to("blog/" + slug + "/")}">{esc(name[lang])}</a></li>'
        for slug, name in svc["reading"])
    out.append(block("read", T["reading"], f'  <ul class="svc-read">{links}</ul>'))

    out.append(block("not", T["not_this"],
        '  <ul class="svc-list svc-list--no">' +
        "".join(f"<li>{esc(x[lang])}</li>" for x in svc["not_this"]) + "</ul>\n"
        f'  <p class="svc-more"><a href="{ctx.to("what-i-take/")}">{T["take"]}</a></p>',
        cls="svc-block--muted"))

    return "\n".join(out)
