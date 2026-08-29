# -*- coding: utf-8 -*-
"""ЯДРО · Сборка страниц.

Страница = оболочка (theme) + список секций. Секция — это либо готовый
двуязычный фрагмент из content/fragments/, либо компонент, собранный из
данных (кейсы, статьи, карточки). Ничего специфичного для конкретной
страницы здесь нет: что именно собирать, описано в content/pages/.
"""
import datetime
import glob
import importlib.util
import os
import re

from . import blocks, config as cfg
from .theme import Ctx, esc, fmt_date, head, header, footer, ticker, jsonld, org_node, person_node, write


# ---------------------------------------------------------------------------
# Загрузка контента
# ---------------------------------------------------------------------------
def _load_dir(sub, var):
    items = []
    for path in sorted(glob.glob(os.path.join(cfg.CONTENT, sub, "*.py"))):
        name = os.path.splitext(os.path.basename(path))[0]
        if name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"{sub}_{name}", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        item = getattr(mod, var)
        item.setdefault("slug", name)
        items.append(item)
    return items


def load_posts():
    posts = _load_dir("posts", "POST")
    for p in posts:
        p.setdefault("updated", p["date"])
        p.setdefault("cover", f"{p['slug']}-cover.png")
    return sorted(posts, key=lambda p: p["date"])


def load_cases():
    return sorted(_load_dir("cases", "CASE"), key=lambda c: c.get("order", 99))


def _load_blocks(name):
    """content/blocks/<name>.py → словарь {"ru": [...], "en": [...]}"""
    path = os.path.join(cfg.CONTENT, "blocks", name + ".py")
    spec = importlib.util.spec_from_file_location(f"blocks_{name}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.BLOCKS


def load_pages():
    return sorted(_load_dir("pages", "PAGE"), key=lambda p: p.get("order", 99))


# ---------------------------------------------------------------------------
# Фрагменты
# ---------------------------------------------------------------------------

# Заголовок главной. Раньше оба языка лежали в одном <h1> и английский просто
# прятался CSS-ом — то есть у /en/ главный заголовок страницы был кириллицей,
# а у обеих версий — наполовину на чужом языке. Теперь H1 рендерится под язык
# страницы, а мгновенное переключение остаётся у всего остального.
HERO_H1 = {
    "ru": ("ПОРЯДОК<br>ИЗ <span class=\"hl\">ХАОСА</span>.<br>БЕЗ ВОДЫ.",
           "Независимый консалтинг, автоматизация процессов и проектный менеджмент"),
    "en": ("ORDER<br>FROM <span class=\"hl\">CHAOS</span>.<br>NO FLUFF.",
           "Independent consulting, process automation and project management"),
}


def hero_h1(lang):
    big, sub = HERO_H1[lang]
    return (f'<h1 class="hero__title">'
            f'<span class="hero__title-main">{big}</span>'
            f'<span class="hero__title-sub">{sub}</span>'
            f'</h1>')

def fragment(name, ctx):
    path = os.path.join(cfg.CONTENT, "fragments", name + ".html")
    s = open(path, encoding="utf-8").read()
    return (s.replace("{{ASSET}}", ctx.asset)
             .replace("{{HOME}}", ctx.to())
             .replace("{{BLOG}}", ctx.to("blog/"))
             .replace("{{CASES}}", ctx.to("cases/"))
             .replace("{{SERVICES}}", ctx.to("services/"))
             .replace("{{HERO_H1}}", hero_h1(ctx.lang))
             .replace("{{PRIVACY}}", ctx.to("privacy/"))
             .replace("{{FORM_ENDPOINT}}", cfg.FORM_ENDPOINT)
             .replace("{{FOUNDER_ALT}}",
                      "основатель Ganza Consulting" if ctx.lang == "ru"
                      else "founder of Ganza Consulting"))


# ---------------------------------------------------------------------------
# Схема из разметки
# ---------------------------------------------------------------------------
def faq_nodes(ctx, name="faq"):
    """FAQPage, собранный регуляркой из самого фрагмента FAQ.

    Смысл ровно в том, чтобы источник был один: вопросы и ответы живут в
    content/fragments/faq.html, а разметка для поиска считается из них. Если
    вопрос отредактируют, схема поедет следом и разойтись им негде.
    """
    path = os.path.join(cfg.CONTENT, "fragments", name + ".html")
    if not os.path.exists(path):
        return []
    src = open(path, encoding="utf-8").read()
    lang = ctx.lang
    qa = []
    for block in re.findall(r"<details[^>]*>(.*?)</details>", src, re.S):
        q = re.search(rf'<summary>.*?<span class="lang-{lang}">(.*?)</span>', block, re.S)
        a = re.search(rf'<p>.*?<span class="lang-{lang}">(.*?)</span>', block, re.S)
        if not (q and a):
            continue
        strip = lambda t: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()
        qa.append((strip(q.group(1)), strip(a.group(1))))
    if not qa:
        return []
    return [{"@type": "FAQPage", "@id": ctx.abs() + "#faq",
             "inLanguage": lang,
             "mainEntity": [{"@type": "Question", "name": q,
                             "acceptedAnswer": {"@type": "Answer", "text": a}}
                            for q, a in qa]}]


def crumbs(ctx, *trail):
    """BreadcrumbList: (название, путь) от главной к текущей странице."""
    items = [{"@type": "ListItem", "position": 1,
              "name": ctx.L["home"], "item": ctx.abs("")}]
    for n, (name, path) in enumerate(trail, start=2):
        items.append({"@type": "ListItem", "position": n,
                      "name": name, "item": ctx.abs(path)})
    return [{"@type": "BreadcrumbList", "@id": ctx.abs() + "#breadcrumb",
             "itemListElement": items}]


# ---------------------------------------------------------------------------
# Компоненты
# ---------------------------------------------------------------------------
def services_teaser(ctx):
    """Компактная полоса услуг для главной. Заголовки берутся из того же
    фрагмента, что и полная секция, — расходиться им негде."""
    src = open(os.path.join(cfg.CONTENT, "fragments", "services.html"), encoding="utf-8").read()
    items = []
    for m in re.finditer(r'data-project-type="([a-z]+)".*?<h3>(.*?)</h3>', src, re.S):
        kind, title = m.group(1), m.group(2).replace("<br>", " ")
        items.append(f"""    <a class="teaser-card" href="{ctx.to('services/')}#services" data-reveal data-track="teaser-{kind}">
      <span class="teaser-card__title">{title}</span>
      <span class="teaser-card__go">→</span>
    </a>""")
    L = ctx.L
    lead = ("Одна сложная задача — и человек, который в ней разберётся. Четыре направления, "
            "в каждом фиксированный объём и цена до старта."
            if ctx.lang == "ru" else
            "One hard problem and the person who'll get to the bottom of it. Four areas, each "
            "with a fixed scope and a price agreed before the work starts.")
    return f"""<section class="teaser" id="services-teaser">
  <div class="section-label">
    <span class="tag tag--blue">{'01 / УСЛУГИ' if ctx.lang == 'ru' else '01 / SERVICES'}</span>
    <h2>{L['services'].upper()}</h2>
    <p class="section-label__intro">{lead}</p>
  </div>
  <div class="teaser__grid">
{chr(10).join(items)}
  </div>
  <p class="teaser__more"><a class="btn btn--outline" href="{ctx.to('services/')}" data-track="all-services">{'ВСЕ УСЛУГИ И ЦЕНЫ →' if ctx.lang == 'ru' else 'ALL SERVICES & PRICING →'}</a></p>
</section>
"""


def case_card(case, ctx):
    L = ctx.L
    tags = "".join(f'<span class="badge">{t}</span>' for t in case.get("tags", []))
    # «Что бы я сделал иначе» — необязательный блок. Кейс без него читается как
    # реклама; с ним — как разбор, и заодно честно называет слабые места цифры.
    honest = ""
    if case.get("honest"):
        label = "ЧЕСТНАЯ ОГОВОРКА" if ctx.lang == "ru" else "THE HONEST CAVEAT"
        honest = (f'      <details class="case-card__honest">\n'
                  f'        <summary>{label}</summary>\n'
                  f'        <p>{esc(case["honest"][ctx.lang])}</p>\n'
                  f'      </details>\n')
    return f"""    <article class="case-card case-card--{case['accent']}" data-reveal>
      <div class="case-card__top">
        <span class="case-card__client">{esc(case['client'][ctx.lang]).upper()}</span>
        <span class="case-card__stat">{esc(case['stat'][ctx.lang])}</span>
      </div>
      <h3>{esc(case['title'][ctx.lang]).upper()}</h3>
      <p class="case-card__label">{L['problem']}</p>
      <p>{esc(case['problem'][ctx.lang])}</p>
      <p class="case-card__label">{L['did']}</p>
      <p>{esc(case['did'][ctx.lang])}</p>
      <p class="case-card__result">→ {esc(case['result'][ctx.lang])}</p>
{honest}      <div class="case-card__tags">{tags}</div>
    </article>"""


def cases_grid(ctx, cases, heading=True, eyebrow="02 / РЕЗУЛЬТАТЫ", more=False):
    cards = "\n".join(case_card(c, ctx) for c in cases)
    label = ""
    if heading:
        eb = eyebrow if ctx.lang == "ru" else eyebrow.replace("РЕЗУЛЬТАТЫ", "RESULTS")
        label = f"""  <div class="section-label">
    <span class="tag tag--yellow">{eb}</span>
    <h2>{ctx.L['cases'].upper()}</h2>
  </div>
"""
    tail = ""
    if more:
        tail = (f'\n  <p class="teaser__more"><a class="btn btn--outline" '
                f'href="{ctx.to("cases/")}" data-track="all-cases">{ctx.L["all_cases"]}</a></p>')
    return f"""<section class="cases" id="cases">
{label}  <div class="cases__grid">
{cards}
  </div>{tail}
</section>
"""


def posts_teaser(ctx, posts, limit=3):
    from .blocks import read_minutes
    latest = list(reversed(posts))[:limit]
    cards = []
    for x in latest:
        mins = read_minutes(x["body"][ctx.lang], ctx.lang, x["h1"][ctx.lang] + x["dek"][ctx.lang])
        cards.append(f"""    <a class="post-card post-card--slim" href="{ctx.to('blog/' + x['slug'] + '/')}" data-reveal data-track="teaser-post-{x['slug']}">
      <span class="post-card__meta">
        <span class="post-card__tag">{esc(x['tag'][ctx.lang])}</span>
        <span>{mins} {ctx.L['min_read']}</span>
      </span>
      <h3>{esc(x['h1'][ctx.lang])}</h3>
      <p class="post-card__excerpt">{esc(x['dek'][ctx.lang])}</p>
    </a>""")
    eb = "03 / БЛОГ" if ctx.lang == "ru" else "03 / BLOG"
    lead = ("Большие разборы без воды — по задачам, которые реально делались."
            if ctx.lang == "ru" else
            "Long-form, no-fluff breakdowns of problems that were actually solved.")
    return f"""<section class="teaser" id="blog-teaser">
  <div class="section-label">
    <span class="tag tag--blue">{eb}</span>
    <h2>{ctx.L['blog'].upper()}</h2>
    <p class="section-label__intro">{lead}</p>
  </div>
  <div class="teaser__grid teaser__grid--posts">
{chr(10).join(cards)}
  </div>
  <p class="teaser__more"><a class="btn btn--outline" href="{ctx.to('blog/')}" data-track="all-posts">{ctx.L['all_posts']}</a></p>
</section>
"""


# ---------------------------------------------------------------------------
# Универсальная сборка страницы из описания
# ---------------------------------------------------------------------------
def page_hero(page, ctx):
    """Заголовок страницы. Без него у документа нет <h1>, а у поиска — темы."""
    h = page.get("hero")
    if not h:
        return ""
    lead = f'<p class="page-hero__lead">{h["lead"][ctx.lang]}</p>' if h.get("lead") else ""
    return f"""<section class="page-hero">
  <span class="tag tag--blue">{h['eyebrow'][ctx.lang]}</span>
  <h1>{h['h1'][ctx.lang]}</h1>
  {lead}
</section>
"""


def render_sections(page, ctx, posts, cases):
    out = [page_hero(page, ctx)]
    for item in page["sections"]:
        kind, arg = (item, None) if isinstance(item, str) else item
        if kind == "fragment":
            out.append(fragment(arg, ctx))
        elif kind == "services_teaser":
            out.append(services_teaser(ctx))
        elif kind == "cases":
            n = arg or len(cases)
            out.append(cases_grid(ctx, cases[:n], more=bool(arg)))
        elif kind == "posts":
            out.append(posts_teaser(ctx, posts, arg or 3))
        elif kind == "blocks":
            # Текстовая страница из того же набора блоков, что и статьи:
            # политика, оферта, «за что не берусь». Ширина и типографика
            # берутся у статьи, поэтому длинный текст читается одинаково.
            data = _load_blocks(arg)
            html = blocks.render(data[ctx.lang], ctx)
            out.append(f'<section class="textpage"><div class="post__body">{html}</div></section>')
        else:
            raise ValueError(f"неизвестная секция: {kind!r}")
    return "\n".join(out)


def build_page(page, ctx, posts, cases):
    graph = [org_node(), person_node(ctx.lang),
             {"@type": "WebPage", "@id": ctx.abs() + "#page",
              "url": ctx.abs(), "name": page["title"][ctx.lang],
              "description": page["description"][ctx.lang],
              "inLanguage": ctx.lang,
              "isPartOf": {"@id": f"{cfg.SITE}/#website"}}]
    graph += page.get("schema", lambda c: [])(ctx)

    html = head(ctx,
                title=esc(page["title"][ctx.lang]),
                description=esc(page["description"][ctx.lang]),
                keywords=esc(page.get("keywords", {}).get(ctx.lang, "")),
                og_image_alt=esc(page["title"][ctx.lang]),
                jsonld=jsonld(graph),
                body_class=f"page-{page.get('slug', 'home') or 'home'}",
                feed=f"{cfg.SITE}/{cfg.LANG_PREFIX[ctx.lang]}blog/feed.xml")
    html += ticker(ctx) + header(ctx, active=page.get("nav_key", ""))
    html += "\n<main id=\"content\">\n"
    html += render_sections(page, ctx, posts, cases)
    html += "\n</main>\n"
    has_builder = page.get("builder", True)
    if has_builder:
        html += fragment("builder-modal", ctx)

    # form.js грузим только там, где форма действительно есть
    scripts = ("builder.js",) if has_builder else ()
    if any((s if isinstance(s, str) else s[1]) == "contact-form"
           for s in page["sections"] if not isinstance(s, str)):
        scripts = scripts + ("form.js",)
    html += footer(ctx, scripts=scripts)

    out = (ctx.url_path or "") + "index.html"
    write(out, html)
    return out
