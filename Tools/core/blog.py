# -*- coding: utf-8 -*-
"""ЯДРО · Блог: лента, статья, RSS.

Статья собирается в три колонки: слева липкое оглавление, по центру текст,
справа мета и «наверх». На узких экранах колонки схлопываются в одну, а
оглавление превращается в раскрывающийся блок над текстом.
"""
import datetime
import re

from . import blocks, config as cfg
from .pages import fragment
from .theme import (Ctx, esc, fmt_date, head, header, footer, ticker,
                    jsonld, org_node, person_node, write)


def read_minutes(post, lang):
    """Считаем всё, что читатель действительно читает: текст, выводы и FAQ."""
    extra = [post["h1"][lang], post["dek"][lang]]
    extra += post.get("takeaways", {}).get(lang, [])
    for q, a in post.get("faq", {}).get(lang, []):
        extra += [q, a]
    return blocks.read_minutes(post["body"][lang], lang, " ".join(extra))


def word_count(post, lang):
    from .theme import count_words
    return count_words(blocks.plain(post["body"][lang]))


# ---------------------------------------------------------------------------
# Куски статьи
# ---------------------------------------------------------------------------
def toc_rail(toc, ctx):
    if len(toc) < 3:
        return ""
    items = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in toc)
    return f"""<div class="rail rail--left">
  <nav class="toc" aria-label="{ctx.L['contents']}">
    <p class="toc__title">{ctx.L['contents']}</p>
    <ol class="toc__list">{items}</ol>
  </nav>
</div>"""


def meta_rail(post, ctx):
    url = ctx.abs()
    title = post["h1"][ctx.lang]
    share = [
        ("Telegram", f"https://t.me/share/url?url={url}&text={esc(title)}"),
        ("LinkedIn", f"https://www.linkedin.com/sharing/share-offsite/?url={url}"),
        ("X", f"https://twitter.com/intent/tweet?url={url}&text={esc(title)}"),
    ]
    links = "".join(
        f'<a href="{u}" target="_blank" rel="noopener" data-track="share-{n.lower()}">{n}</a>'
        for n, u in share)
    return f"""<div class="rail rail--right">
  <div class="rail__block">
    <p class="rail__label">{ctx.L['min_read'].upper()}</p>
    <p class="rail__value">{read_minutes(post, ctx.lang)}</p>
  </div>
  <div class="rail__block">
    <p class="rail__label">{ctx.L['share']}</p>
    <div class="rail__share">{links}</div>
  </div>
  <a class="rail__top" href="#top">{ctx.L['top']}</a>
</div>"""


def takeaways(post, ctx):
    items = post.get("takeaways", {}).get(ctx.lang, [])
    if not items:
        return ""
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f"""<div class="post__takeaways" data-reveal>
    <p class="post__takeaways-title">{ctx.L['takeaways']}</p>
    <ul>{lis}</ul>
  </div>"""


def faq_section(post, ctx):
    items = post.get("faq", {}).get(ctx.lang, [])
    if not items:
        return ""
    body = "".join(f"""<details class="faq-item">
      <summary>{esc(q)}<span class="faq-item__icon" aria-hidden="true"></span></summary>
      <p>{blocks.resolve(a, ctx)}</p>
    </details>""" for q, a in items)
    return f"""<section class="post__faq" id="faq" data-reveal>
    <h2>{ctx.L['faq']}</h2>
    <div class="faq__list">{body}</div>
  </section>"""


def author_box(ctx):
    return f"""<section class="post__author" data-reveal>
    <picture>
      <source srcset="{ctx.asset}img/founder-sm.webp" type="image/webp">
      <img src="{ctx.asset}img/founder-sm.jpg" width="120" height="160" alt="{esc(cfg.AUTHOR_NAME)}" loading="lazy" decoding="async">
    </picture>
    <div>
      <p class="post__author-label">{ctx.L['author']}</p>
      <p class="post__author-name">{esc(cfg.AUTHOR_NAME)}</p>
      <p class="post__author-bio">{esc(cfg.AUTHOR_BIO[ctx.lang])}</p>
      <p class="post__author-links">
        <a href="{cfg.TELEGRAM}" target="_blank" rel="noopener" data-track="author-telegram">Telegram ↗</a>
        <a href="{ctx.to()}#about">{ctx.L['home']} ↗</a>
      </p>
    </div>
  </section>"""


# ---------------------------------------------------------------------------
# Страница статьи
# ---------------------------------------------------------------------------
def build_post(post, posts, lang):
    ctx = Ctx(lang, f"blog/{post['slug']}/")
    L = ctx.L
    i = posts.index(post)
    body, toc = blocks.render(post["body"][lang], ctx, collect_toc=True)

    extra_meta = "\n".join(
        [f'<meta property="article:published_time" content="{post["date"]}">',
         f'<meta property="article:modified_time" content="{post["updated"]}">',
         f'<meta property="article:section" content="{esc(post["tag"][lang])}">']
        + [f'<meta property="article:tag" content="{esc(t)}">' for t in post["hashtags"]])

    cover = f"{cfg.SITE}/{cfg.ASSETS}/img/blog/{post['cover']}"
    graph = [org_node(), person_node(lang),
             {"@type": "BreadcrumbList", "@id": ctx.abs() + "#breadcrumb",
              "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": L["home"], "item": ctx.abs("")},
                  {"@type": "ListItem", "position": 2, "name": L["blog"], "item": ctx.abs("blog/")},
                  {"@type": "ListItem", "position": 3, "name": post["h1"][lang], "item": ctx.abs()}]},
             {"@type": "BlogPosting", "@id": ctx.abs() + "#article",
              "headline": post["h1"][lang], "alternativeHeadline": post["dek"][lang],
              "description": post["description"][lang], "articleSection": post["tag"][lang],
              "keywords": post["keywords"][lang], "inLanguage": lang,
              "wordCount": word_count(post, lang),
              "timeRequired": f"PT{read_minutes(post, lang)}M",
              "image": {"@type": "ImageObject", "url": cover, "width": 1200, "height": 630},
              "datePublished": post["date"], "dateModified": post["updated"],
              "author": {"@id": f"{cfg.SITE}/#george-mercer"},
              "publisher": {"@id": f"{cfg.SITE}/#organization"},
              "mainEntityOfPage": {"@type": "WebPage", "@id": ctx.abs()}}]
    faq = post.get("faq", {}).get(lang, [])
    if faq:
        graph.append({"@type": "FAQPage", "@id": ctx.abs() + "#faq",
                      "mainEntity": [{"@type": "Question", "name": q,
                                      "acceptedAnswer": {"@type": "Answer",
                                                         "text": re.sub(r"<[^>]+>", "", a)}}
                                     for q, a in faq]})

    html = head(ctx, title=esc(post["title"][lang]),
                description=esc(post["description"][lang]),
                keywords=esc(post["keywords"][lang]),
                og_image=cover, og_image_alt=esc(post["h1"][lang]),
                og_type="article", jsonld=jsonld(graph), extra_meta=extra_meta,
                body_class="page-article",
                feed=ctx.abs("blog/feed.xml"))
    html += ticker(ctx) + header(ctx, active="blog")

    prev_post = posts[i - 1] if i > 0 else posts[-1]
    next_post = posts[i + 1] if i < len(posts) - 1 else posts[0]
    related = [q for q in posts if q["slug"] in post.get("related", []) and q is not post][:3]
    related_html = ""
    if related:
        cards = "".join(f"""<a class="related-card" href="../{r['slug']}/" data-reveal data-track="related-{r['slug']}">
        <span class="related-card__tag">{esc(r['tag'][lang])}</span>
        <span class="related-card__title">{esc(r['h1'][lang])}</span>
        <span class="related-card__meta">{read_minutes(r, lang)} {L['min_read']}</span>
      </a>""" for r in related)
        related_html = f"""<section class="post__related">
    <h2>{L['related']}</h2>
    <div class="post__related-grid">{cards}</div>
  </section>"""

    updated = (f' · {L["updated"]} {fmt_date(post["updated"], lang)}'
               if post["updated"] != post["date"] else "")
    tags = "".join(f'<span class="badge">#{h}</span>' for h in post["hashtags"])

    html += f"""
<main id="content" class="post-wrap">
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <a href="{ctx.to()}">{L['home']}</a><span>/</span><a href="{ctx.to('blog/')}">{L['blog']}</a><span>/</span><span aria-current="page">{esc(post['h1'][lang])}</span>
</nav>

<article class="post">
  <div class="post__head">
    <div class="post__meta">
      <span class="post__tag">{esc(post['tag'][lang])}</span>
      <span>{read_minutes(post, lang)} {L['min_read']} · {fmt_date(post['date'], lang)}{updated}</span>
    </div>
    <h1>{esc(post['h1'][lang])}</h1>
    <p class="post__dek">{esc(post['dek'][lang])}</p>
  </div>

  <div class="post-shell">
    {toc_rail(toc, ctx)}

    <div class="post__body">
        {body}

  {takeaways(post, ctx)}

  {faq_section(post, ctx)}

  <div class="post__tags">{tags}</div>

  {author_box(ctx)}

  <div class="post__cta" data-reveal>
    <div class="post__cta-box">
      <p>{L['cta_text']}</p>
      <a class="btn btn--yellow" href="#contact-form" data-track="post-cta-form">{L['cta_form']}</a>
      <a class="btn btn--outline" href="{cfg.TELEGRAM}" target="_blank" rel="noopener" data-track="post-cta-telegram">{L['cta_tg']}</a>
      <a class="btn btn--outline" href="{ctx.to('services/')}#pricing" data-track="post-cta-pricing">{L['cta_pricing']}</a>
    </div>
  </div>
    </div>

    {meta_rail(post, ctx)}
  </div>
</article>

{related_html}

<nav class="post__nav">
  <a class="post__nav-link" href="../{prev_post['slug']}/" data-track="post-prev">
    <span class="post__nav-label">{L['prev']}</span>
    <span class="post__nav-title">{esc(prev_post['h1'][lang])}</span>
  </a>
  <a class="post__nav-link" href="../{next_post['slug']}/" data-track="post-next">
    <span class="post__nav-label">{L['next']}</span>
    <span class="post__nav-title">{esc(next_post['h1'][lang])}</span>
  </a>
</nav>

{fragment("contact-form", ctx)}
</main>
"""
    html += footer(ctx, scripts=("form",))
    out = ctx.url_path + "index.html"
    write(out, html)
    return out


# ---------------------------------------------------------------------------
# Лента
# ---------------------------------------------------------------------------
INDEX_COPY = {
    "en": dict(
        title="Blog — Consulting, Automation and Project Management",
        h1="NOTES ON HARD PROBLEMS",
        description="Long-form, no-fluff articles on consulting, process automation and AI, "
                    "project management and web development — written from delivered engagements.",
        intro="Long-form notes written by the person who does the work. Every article ends with "
              "something you can act on, not a list of things to consider.",
        count="{n} articles · {mins} minutes of reading",
    ),
    "ru": dict(
        title="Блог — консалтинг, автоматизация, проектный менеджмент",
        h1="ЗАМЕТКИ О СЛОЖНЫХ ЗАДАЧАХ",
        description="Большие статьи без воды о консалтинге, автоматизации и ИИ, проектном "
                    "менеджменте и веб-разработке — по реальным проектам, а не по контент-плану.",
        intro="Большие заметки от человека, который сам делает работу. Каждая статья "
              "заканчивается тем, что можно применить, а не списком «вопросов к обсуждению».",
        count="{n} статей · {mins} минут чтения",
    ),
}


def build_index(posts, lang):
    ctx = Ctx(lang, "blog/")
    L, C = ctx.L, INDEX_COPY[lang]
    ordered = list(reversed(posts))
    total = sum(read_minutes(x, lang) for x in ordered)

    tags = []
    for x in ordered:
        if x["tag"][lang] not in tags:
            tags.append(x["tag"][lang])
    chips = f'<button class="blog-filter__btn is-active" type="button" data-filter="*">{L["filter_all"]}</button>'
    chips += "".join(f'<button class="blog-filter__btn" type="button" data-filter="{esc(t)}">{esc(t)}</button>'
                     for t in tags)

    # Первые две карточки — над сгибом, они и есть кандидаты в LCP. Отложенная
    # загрузка LCP-картинки стабильно добавляет к нему сотни миллисекунд, так
    # что первым двум ставим eager + высокий приоритет, остальным — lazy.
    def _load(i):
        return ('loading="eager" fetchpriority="high"' if i < 2
                else 'loading="lazy" fetchpriority="low"')

    cards = "\n".join(f"""    <a class="post-card" href="{x['slug']}/" data-tag="{esc(x['tag'][lang])}" data-reveal data-track="card-{x['slug']}">
      <span class="post-card__cover">
        <img src="{ctx.asset}img/blog/{x['slug']}-card.webp" width="760" height="399" {_load(i)} decoding="async" alt="{esc(x['h1'][lang])}">
      </span>
      <span class="post-card__meta">
        <span class="post-card__tag">{esc(x['tag'][lang])}</span>
        <span>{read_minutes(x, lang)} {L['min_read']} · {fmt_date(x['date'], lang)}</span>
      </span>
      <h2>{esc(x['h1'][lang])}</h2>
      <p class="post-card__excerpt">{esc(x['dek'][lang])}</p>
      <span class="post-card__cta">{L['read_article']}</span>
    </a>""" for i, x in enumerate(ordered))

    graph = [org_node(), person_node(lang),
             {"@type": "Blog", "@id": ctx.abs() + "#blog", "url": ctx.abs(),
              "name": f"{cfg.BRAND} — {L['blog']}", "description": C["description"],
              "inLanguage": lang, "publisher": {"@id": f"{cfg.SITE}/#organization"},
              "author": {"@id": f"{cfg.SITE}/#george-mercer"}},
             {"@type": "BreadcrumbList", "@id": ctx.abs() + "#breadcrumb",
              "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": L["home"], "item": ctx.abs("")},
                  {"@type": "ListItem", "position": 2, "name": L["blog"], "item": ctx.abs()}]},
             {"@type": "ItemList", "@id": ctx.abs() + "#list",
              "itemListElement": [{"@type": "ListItem", "position": n + 1,
                                   "url": ctx.abs(f"blog/{x['slug']}/"), "name": x["h1"][lang]}
                                  for n, x in enumerate(ordered)]}]

    html = head(ctx, title=esc(C["title"]), description=esc(C["description"]),
                og_image_alt=esc(C["h1"]), jsonld=jsonld(graph),
                body_class="page-blog", feed=ctx.abs("blog/feed.xml"))
    html += ticker(ctx) + header(ctx, active="blog")
    html += f"""
<main id="content">
<section class="blog-hero">
  <span class="tag tag--blue">{L['blog'].upper()}</span>
  <h1>{C['h1']}</h1>
  <p class="blog-hero__intro">{C['intro']}</p>
  <p class="blog-hero__count">{C['count'].format(n=len(ordered), mins=total)}</p>
</section>

<div class="blog-filter" role="group">{chips}</div>

<section class="blog__grid">
{cards}
</section>
</main>
"""
    html += footer(ctx)
    write(ctx.url_path + "index.html", html)


def build_feed(posts, lang):
    ctx = Ctx(lang, "blog/")
    C = INDEX_COPY[lang]
    items = "\n".join(f"""  <item>
    <title>{esc(x['h1'][lang])}</title>
    <link>{ctx.abs(f"blog/{x['slug']}/")}</link>
    <guid isPermaLink="true">{ctx.abs(f"blog/{x['slug']}/")}</guid>
    <pubDate>{datetime.datetime.strptime(x['date'], '%Y-%m-%d').strftime('%a, %d %b %Y 09:00:00 +0000')}</pubDate>
    <category>{esc(x['tag'][lang])}</category>
    <description>{esc(x['description'][lang])}</description>
  </item>""" for x in reversed(posts))

    write(ctx.url_path + "feed.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{esc(cfg.BRAND)} — {ctx.L['blog']}</title>
  <link>{ctx.abs()}</link>
  <atom:link href="{ctx.abs('blog/feed.xml')}" rel="self" type="application/rss+xml"/>
  <description>{esc(C['description'])}</description>
  <language>{lang}</language>
  <lastBuildDate>{datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')}</lastBuildDate>
{items}
</channel>
</rss>
""")
