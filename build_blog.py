#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bilingual blog generator.

    /blog/                      — English index
    /blog/<slug>/               — English article
    /blog/feed.xml              — English RSS
    /ru/blog/                   — Russian index
    /ru/blog/<slug>/            — Russian article
    /ru/blog/feed.xml           — Russian RSS

Content lives in content/posts/<slug>.py, one module per article, each with a
POST dict holding both languages. Nothing about layout or SEO markup lives in
the content files — add an article, run this, done.

Run:  python3 build_blog.py
"""
import glob
import importlib.util
import json
import math
import os
import re
import datetime

from buildlib import (SITE, BRAND, LABELS, WPM, AUTHOR_NAME, AUTHOR_BIO, TELEGRAM,
                      build_head, jsonld_block, org_node, person_node, ticker, header,
                      footer, fmt_date, count_words, esc, write, ROOT)

LANGS = ("en", "ru")

# ---------------------------------------------------------------------------
# Load content modules, ordered oldest → newest
# ---------------------------------------------------------------------------
def load_posts():
    posts = []
    for path in sorted(glob.glob(os.path.join(ROOT, "content", "posts", "*.py"))):
        name = os.path.splitext(os.path.basename(path))[0]
        if name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"post_{name}", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        post = mod.POST
        post.setdefault("slug", name)
        post.setdefault("updated", post["date"])
        post.setdefault("cover", f"{post['slug']}-cover.png")
        posts.append(post)
    posts.sort(key=lambda p: p["date"])
    return posts


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
TRANSLIT = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh",
    "з": "z", "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o",
    "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "ts",
    "ч": "ch", "ш": "sh", "щ": "sch", "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu",
    "я": "ya",
}


def anchor(text):
    text = re.sub(r"<[^>]+>", "", text).lower()
    text = "".join(TRANSLIT.get(ch, ch) for ch in text)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:60] or "section"


def resolve(text, home, blogroot):
    return text.replace("{{HOME}}", home).replace("{{BLOG}}", blogroot)


def post_text(post, lang):
    """Everything a reader actually reads — used for the reading-time figure."""
    chunks = [post["h1"][lang], post["dek"][lang]]
    for kind, content in post["body"][lang]:
        if kind in ("ul", "ol", "checklist"):
            chunks.extend(content)
        elif kind == "steps":
            for t, b in content:
                chunks += [t, b]
        elif kind == "table":
            chunks.extend(content.get("head", []))
            for row in content.get("rows", []):
                chunks.extend(row)
            chunks.append(content.get("caption", ""))
        else:
            chunks.append(content)
    chunks.extend(post.get("takeaways", {}).get(lang, []))
    for q, a in post.get("faq", {}).get(lang, []):
        chunks += [q, a]
    return " ".join(chunks)


def read_minutes(post, lang):
    return max(2, round(count_words(post_text(post, lang)) / WPM[lang]))


def word_total(post, lang):
    return count_words(post_text(post, lang))


# ---------------------------------------------------------------------------
# Body rendering
# ---------------------------------------------------------------------------
def render_body(post, lang, home, blogroot):
    out, toc = [], []
    for kind, content in post["body"][lang]:
        if kind == "h2":
            a = anchor(content)
            toc.append((a, content))
            out.append(f'<h2 id="{a}">{resolve(content, home, blogroot)}</h2>')
        elif kind == "h3":
            out.append(f'<h3 id="{anchor(content)}">{resolve(content, home, blogroot)}</h3>')
        elif kind == "p":
            out.append(f"<p>{resolve(content, home, blogroot)}</p>")
        elif kind == "ul":
            items = "".join(f"<li>{resolve(li, home, blogroot)}</li>" for li in content)
            out.append(f"<ul>{items}</ul>")
        elif kind == "ol":
            items = "".join(f"<li>{resolve(li, home, blogroot)}</li>" for li in content)
            out.append(f"<ol>{items}</ol>")
        elif kind == "checklist":
            items = "".join(f"<li>{resolve(li, home, blogroot)}</li>" for li in content)
            out.append(f'<ul class="post__checklist">{items}</ul>')
        elif kind == "q":
            out.append(f'<blockquote class="post__pull">{resolve(content, home, blogroot)}</blockquote>')
        elif kind == "note":
            out.append(f'<div class="post__note">{resolve(content, home, blogroot)}</div>')
        elif kind == "steps":
            lis = "".join(
                f'<li><strong>{resolve(t, home, blogroot)}</strong>'
                f'<span>{resolve(b, home, blogroot)}</span></li>'
                for t, b in content
            )
            out.append(f'<ol class="post__steps">{lis}</ol>')
        elif kind == "table":
            head = "".join(f"<th scope=\"col\">{h}</th>" for h in content["head"])
            rows = "".join(
                "<tr>" + "".join(f"<td>{resolve(c, home, blogroot)}</td>" for c in row) + "</tr>"
                for row in content["rows"]
            )
            caption = f'<caption>{content["caption"]}</caption>' if content.get("caption") else ""
            out.append(
                '<div class="post__table-wrap"><table class="post__table">'
                f"{caption}<thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>"
            )
        else:
            raise ValueError(f"unknown block type {kind!r} in {post['slug']}")
    return "\n        ".join(out), toc


def render_toc(toc, lang):
    if len(toc) < 3:
        return ""
    items = "".join(f'<li><a href="#{a}">{re.sub(r"<[^>]+>", "", t)}</a></li>' for a, t in toc)
    return f"""<nav class="post__toc" aria-label="{LABELS[lang]['contents']}">
    <p class="post__toc-title">{LABELS[lang]['contents']}</p>
    <ol>{items}</ol>
  </nav>"""


def render_takeaways(post, lang):
    items = post.get("takeaways", {}).get(lang, [])
    if not items:
        return ""
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f"""<div class="post__takeaways">
    <p class="post__takeaways-title">{LABELS[lang]['takeaways']}</p>
    <ul>{lis}</ul>
  </div>"""


def render_faq(post, lang, home, blogroot):
    items = post.get("faq", {}).get(lang, [])
    if not items:
        return ""
    blocks = "".join(
        f"""<details class="faq-item">
      <summary>{esc(q)}<span class="faq-item__icon" aria-hidden="true"></span></summary>
      <p>{resolve(a, home, blogroot)}</p>
    </details>"""
        for q, a in items
    )
    return f"""<section class="post__faq" id="faq">
    <h2>{LABELS[lang]['faq']}</h2>
    <div class="faq__list">{blocks}</div>
  </section>"""


def render_author(lang, home, p):
    return f"""<section class="post__author">
    <img src="{p}img/founder.png" width="96" height="96" alt="{esc(AUTHOR_NAME)}" loading="lazy" decoding="async">
    <div>
      <p class="post__author-label">{LABELS[lang]['author']}</p>
      <p class="post__author-name">{esc(AUTHOR_NAME)}</p>
      <p class="post__author-bio">{esc(AUTHOR_BIO[lang])}</p>
      <p class="post__author-links">
        <a href="{TELEGRAM}" target="_blank" rel="noopener" data-track="author-telegram">Telegram ↗</a>
        <a href="{home}#about">{LABELS[lang]['nav_about']} ↗</a>
      </p>
    </div>
  </section>"""


# ---------------------------------------------------------------------------
# JSON-LD
# ---------------------------------------------------------------------------
def article_graph(post, lang, canonical, blog_url, home_url):
    body_words = word_total(post, lang)
    graph = [
        org_node(),
        person_node(lang),
        {
            "@type": "BreadcrumbList",
            "@id": f"{canonical}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": LABELS[lang]["home"], "item": home_url},
                {"@type": "ListItem", "position": 2, "name": LABELS[lang]["blog"], "item": blog_url},
                {"@type": "ListItem", "position": 3, "name": post["h1"][lang], "item": canonical},
            ],
        },
        {
            "@type": "BlogPosting",
            "@id": f"{canonical}#article",
            "headline": post["h1"][lang],
            "alternativeHeadline": post["dek"][lang],
            "description": post["description"][lang],
            "articleSection": post["tag"][lang],
            "keywords": post["keywords"][lang],
            "inLanguage": lang,
            "wordCount": body_words,
            "timeRequired": f"PT{read_minutes(post, lang)}M",
            "image": {
                "@type": "ImageObject",
                "url": f"{SITE}/img/blog/{post['cover']}",
                "width": 1200, "height": 630,
            },
            "datePublished": post["date"],
            "dateModified": post["updated"],
            "author": {"@id": f"{SITE}/#george-mercer"},
            "publisher": {"@id": f"{SITE}/#organization"},
            "isPartOf": {"@id": f"{blog_url}#blog"},
            "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        },
    ]
    faq = post.get("faq", {}).get(lang, [])
    if faq:
        graph.append({
            "@type": "FAQPage",
            "@id": f"{canonical}#faq",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
                for q, a in faq
            ],
        })
    return graph


# ---------------------------------------------------------------------------
# Article page
# ---------------------------------------------------------------------------
def build_post(post, posts, lang):
    i = posts.index(post)
    slug = post["slug"]
    p = "../../" if lang == "en" else "../../../"
    home = "../../"          # /blog/<slug>/ → /   and   /ru/blog/<slug>/ → /ru/
    blogroot = "../"
    prefix = "" if lang == "en" else "ru/"
    canonical = f"{SITE}/{prefix}blog/{slug}/"
    blog_url = f"{SITE}/{prefix}blog/"
    home_url = f"{SITE}/" if lang == "en" else f"{SITE}/ru/"
    alt_lang = "ru" if lang == "en" else "en"
    alt_url = f"../../ru/blog/{slug}/" if lang == "en" else f"../../../blog/{slug}/"

    body_html, toc = render_body(post, lang, home, blogroot)

    extra_meta = "\n".join([
        f'<meta property="article:published_time" content="{post["date"]}">',
        f'<meta property="article:modified_time" content="{post["updated"]}">',
        f'<meta property="article:author" content="{esc(AUTHOR_NAME)}">',
        f'<meta property="article:section" content="{esc(post["tag"][lang])}">',
    ] + [f'<meta property="article:tag" content="{esc(t)}">' for t in post["hashtags"]])

    head = build_head(
        lang=lang,
        title=esc(post["title"][lang]),
        description=esc(post["description"][lang]),
        keywords=esc(post["keywords"][lang]),
        canonical=canonical,
        alt_urls={"en": f"{SITE}/blog/{slug}/", "ru": f"{SITE}/ru/blog/{slug}/"},
        og_image=f"{SITE}/img/blog/{post['cover']}",
        og_image_alt=esc(post["h1"][lang]),
        og_type="article",
        p=p,
        jsonld=jsonld_block(article_graph(post, lang, canonical, blog_url, home_url)),
        extra_meta=extra_meta,
        css=("style", "builder", "blog", "glass"),
        feed=f"{blog_url}feed.xml",
    )

    L = LABELS[lang]
    prev_post = posts[i - 1] if i > 0 else posts[-1]
    next_post = posts[i + 1] if i < len(posts) - 1 else posts[0]
    tags_html = "".join(f'<span class="badge">#{h}</span>' for h in post["hashtags"])

    related = [q for q in posts if q["slug"] in post.get("related", []) and q["slug"] != slug][:3]
    related_html = ""
    if related:
        cards = "".join(
            f"""<a class="related-card" href="../{r['slug']}/" data-track="related-{r['slug']}">
        <span class="related-card__tag">{esc(r['tag'][lang])}</span>
        <span class="related-card__title">{esc(r['h1'][lang])}</span>
        <span class="related-card__meta">{read_minutes(r, lang)} {L['min_read']}</span>
      </a>"""
            for r in related
        )
        related_html = f"""<section class="post__related">
    <h2>{L['related']}</h2>
    <div class="post__related-grid">{cards}</div>
  </section>"""

    updated_html = ""
    if post["updated"] != post["date"]:
        updated_html = f' · {L["updated"]} {fmt_date(post["updated"], lang)}'

    html = head + '<body class="page-article">\n' + ticker(lang)
    html += header(lang, p, home, blogroot, alt_url, active="blog")
    html += f"""
<main class="post-wrap">
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <a href="{home}">{L['home']}</a><span>/</span><a href="{blogroot}">{L['blog']}</a><span>/</span><span aria-current="page">{esc(post['h1'][lang])}</span>
</nav>

<article class="post">
  <div class="post__head">
    <div class="post__meta">
      <span class="post__tag">{esc(post['tag'][lang])}</span>
      <span>{read_minutes(post, lang)} {L['min_read']} · {fmt_date(post['date'], lang)}{updated_html}</span>
    </div>
    <h1>{esc(post['h1'][lang])}</h1>
    <p class="post__dek">{esc(post['dek'][lang])}</p>
  </div>

  {render_toc(toc, lang)}

  <div class="post__body">
        {body_html}
  </div>

  {render_takeaways(post, lang)}

  {render_faq(post, lang, home, blogroot)}

  <div class="post__tags">{tags_html}</div>

  {render_author(lang, home, p)}

  <div class="post__cta">
    <div class="post__cta-box">
      <p>{L['cta_text']}</p>
      <a class="btn btn--yellow" href="{TELEGRAM}" target="_blank" rel="noopener" data-track="post-cta-telegram">{L['cta_tg']}</a>
      <a class="btn btn--outline" href="{home}#pricing" data-track="post-cta-pricing">{L['cta_pricing']}</a>
    </div>
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
</main>
"""
    html += footer(lang, p)
    out = f"{prefix}blog/{slug}/index.html"
    write(out, html)
    return read_minutes(post, lang), word_total(post, lang)


# ---------------------------------------------------------------------------
# Blog index
# ---------------------------------------------------------------------------
INDEX_COPY = {
    "en": dict(
        title="Blog — Consulting, Automation and Project Management",
        h1="NOTES ON HARD PROBLEMS",
        description="Long-form, no-fluff articles on consulting, process automation and AI, project management and web development — written from delivered engagements.",
        keywords="business consulting blog, process automation articles, project management insights, digital transformation case studies, consulting advice for founders, AI automation guide",
        intro="Long-form notes on consulting, automation, project management and web development — written by the person who does the work. Every article ends with something you can act on, not a list of things to consider.",
        count="{n} articles · {mins} minutes of reading",
    ),
    "ru": dict(
        title="Блог — консалтинг, автоматизация, проектный менеджмент",
        h1="ЗАМЕТКИ О СЛОЖНЫХ ЗАДАЧАХ",
        description="Большие статьи без воды о консалтинге, автоматизации и ИИ, проектном менеджменте и веб-разработке — по реальным проектам, а не по контент-плану.",
        keywords="блог о бизнес-консалтинге, статьи об автоматизации процессов, проектный менеджмент статьи, цифровая трансформация кейсы, советы консультанта для основателей, внедрение ИИ в бизнес",
        intro="Большие заметки о консалтинге, автоматизации, управлении проектами и веб-разработке — от человека, который сам делает работу. Каждая статья заканчивается тем, что можно применить, а не списком «вопросов к обсуждению».",
        count="{n} статей · {mins} минут чтения",
    ),
}


def build_index(posts, lang):
    p = "../" if lang == "en" else "../../"
    home = "../"
    blogroot = "./"
    prefix = "" if lang == "en" else "ru/"
    canonical = f"{SITE}/{prefix}blog/"
    alt_url = "../ru/blog/" if lang == "en" else "../../blog/"
    L = LABELS[lang]
    C = INDEX_COPY[lang]

    ordered = list(reversed(posts))
    total_mins = sum(read_minutes(x, lang) for x in ordered)

    tags = []
    for x in ordered:
        if x["tag"][lang] not in tags:
            tags.append(x["tag"][lang])
    chips = f'<button class="blog-filter__btn is-active" type="button" data-filter="*">{L["filter_all"]}</button>'
    chips += "".join(
        f'<button class="blog-filter__btn" type="button" data-filter="{esc(t)}">{esc(t)}</button>'
        for t in tags
    )

    cards = []
    for x in ordered:
        cards.append(f"""    <a class="post-card" href="{x['slug']}/" data-tag="{esc(x['tag'][lang])}" data-track="card-{x['slug']}">
      <span class="post-card__cover">
        <img src="{p}img/blog/{x['slug']}-card.webp" width="760" height="399" loading="lazy" decoding="async" alt="{esc(x['h1'][lang])}">
      </span>
      <span class="post-card__meta">
        <span class="post-card__tag">{esc(x['tag'][lang])}</span>
        <span>{read_minutes(x, lang)} {L['min_read']} · {fmt_date(x['date'], lang)}</span>
      </span>
      <h2>{esc(x['h1'][lang])}</h2>
      <p class="post-card__excerpt">{esc(x['dek'][lang])}</p>
      <span class="post-card__cta">{'READ THE ARTICLE →' if lang == 'en' else 'ЧИТАТЬ СТАТЬЮ →'}</span>
    </a>""")

    graph = [
        org_node(),
        person_node(lang),
        {
            "@type": "Blog",
            "@id": f"{canonical}#blog",
            "url": canonical,
            "name": f"{BRAND} — {L['blog']}",
            "description": C["description"],
            "inLanguage": lang,
            "publisher": {"@id": f"{SITE}/#organization"},
            "author": {"@id": f"{SITE}/#george-mercer"},
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"{canonical}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": L["home"],
                 "item": f"{SITE}/" if lang == "en" else f"{SITE}/ru/"},
                {"@type": "ListItem", "position": 2, "name": L["blog"], "item": canonical},
            ],
        },
        {
            "@type": "ItemList",
            "@id": f"{canonical}#list",
            "itemListElement": [
                {"@type": "ListItem", "position": n + 1,
                 "url": f"{SITE}/{prefix}blog/{x['slug']}/",
                 "name": x["h1"][lang]}
                for n, x in enumerate(ordered)
            ],
        },
    ]

    head = build_head(
        lang=lang,
        title=esc(C["title"]),
        description=esc(C["description"]),
        keywords=esc(C["keywords"]),
        canonical=canonical,
        alt_urls={"en": f"{SITE}/blog/", "ru": f"{SITE}/ru/blog/"},
        og_image=f"{SITE}/img/og-cover.png",
        og_image_alt=esc(C["h1"]),
        og_type="website",
        p=p,
        jsonld=jsonld_block(graph),
        css=("style", "builder", "blog", "glass"),
        feed=f"{canonical}feed.xml",
    )

    html = head + '<body class="page-blog">\n' + ticker(lang)
    html += header(lang, p, home, blogroot, alt_url, active="blog")
    html += f"""
<main>
<section class="blog-hero">
  <span class="tag tag--blue">{L['blog'].upper()}</span>
  <h1>{C['h1']}</h1>
  <p class="blog-hero__intro">{C['intro']}</p>
  <p class="blog-hero__count">{C['count'].format(n=len(ordered), mins=total_mins)}</p>
</section>

<div class="blog-filter" role="group">{chips}</div>

<section class="blog__grid">
{chr(10).join(cards)}
</section>
</main>
"""
    html += footer(lang, p)
    write(f"{prefix}blog/index.html", html)


# ---------------------------------------------------------------------------
# RSS
# ---------------------------------------------------------------------------
def build_feed(posts, lang):
    prefix = "" if lang == "en" else "ru/"
    blog_url = f"{SITE}/{prefix}blog/"
    C = INDEX_COPY[lang]
    items = []
    for x in reversed(posts):
        url = f"{blog_url}{x['slug']}/"
        pub = datetime.datetime.strptime(x["date"], "%Y-%m-%d").strftime("%a, %d %b %Y 09:00:00 +0000")
        items.append(f"""  <item>
    <title>{esc(x['h1'][lang])}</title>
    <link>{url}</link>
    <guid isPermaLink="true">{url}</guid>
    <pubDate>{pub}</pubDate>
    <category>{esc(x['tag'][lang])}</category>
    <description>{esc(x['description'][lang])}</description>
  </item>""")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{esc(BRAND)} — {LABELS[lang]['blog']}</title>
  <link>{blog_url}</link>
  <atom:link href="{blog_url}feed.xml" rel="self" type="application/rss+xml"/>
  <description>{esc(C['description'])}</description>
  <language>{lang}</language>
  <lastBuildDate>{datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')}</lastBuildDate>
{chr(10).join(items)}
</channel>
</rss>
"""
    write(f"{prefix}blog/feed.xml", xml)


def main():
    posts = load_posts()
    if not posts:
        raise SystemExit("no posts found in content/posts/")
    report = []
    for lang in LANGS:
        for post in posts:
            mins, words = build_post(post, posts, lang)
            report.append((lang, post["slug"], mins, words))
        build_index(posts, lang)
        build_feed(posts, lang)

    print(f"{len(posts)} articles × {len(LANGS)} languages\n")
    print(f"{'lang':<5} {'slug':<44} {'min':>4} {'words':>7}")
    for lang, slug, mins, words in report:
        flag = "" if 7 <= mins <= 15 else "  <-- outside 7–15 min"
        print(f"{lang:<5} {slug:<44} {mins:>4} {words:>7}{flag}")


if __name__ == "__main__":
    main()
