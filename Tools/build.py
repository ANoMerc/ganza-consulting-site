#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Собрать весь сайт одной командой.

    python3 Tools/build.py

Пересобирает все страницы на всех языках, ленту блога, RSS, sitemap, robots
и редиректы со старых адресов. Идемпотентно: результат зависит только от
содержимого content/ и настроек в Tools/core/config.py.
"""
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core import assets, blog, config as cfg, pages
from core.theme import Ctx, set_assets, write


# ---------------------------------------------------------------------------
def build_sitemap(posts):
    """Каждый URL перечислен со всеми языковыми парами hreflang."""
    today = datetime.date.today().isoformat()
    urls = []

    def add(path, lastmod, priority, freq):
        alts = "\n".join(
            f'    <xhtml:link rel="alternate" hreflang="{l}" href="{cfg.SITE}/{cfg.LANG_PREFIX[l]}{path}"/>'
            for l in cfg.LANGS)
        alts += (f'\n    <xhtml:link rel="alternate" hreflang="x-default" '
                 f'href="{cfg.SITE}/{cfg.LANG_PREFIX[cfg.DEFAULT_LANG]}{path}"/>')
        for lang in cfg.LANGS:
            urls.append(f"""  <url>
    <loc>{cfg.SITE}/{cfg.LANG_PREFIX[lang]}{path}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
{alts}
  </url>""")

    add("", today, "1.0", "weekly")
    for page in pages.load_pages():
        if page["slug"]:
            add(page["slug"], today, "0.9", "monthly")
    add("blog/", today, "0.9", "weekly")
    for post in sorted(posts, key=lambda p: p["date"], reverse=True):
        add(f"blog/{post['slug']}/", post["updated"], "0.8", "monthly")

    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
          '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + "\n".join(urls) + "\n</urlset>\n")
    return len(urls)


def build_robots():
    write("robots.txt", f"""User-agent: *
Allow: /
Disallow: /admin/
Disallow: /Tools/
Disallow: /content/

Sitemap: {cfg.SITE}/sitemap.xml
""")
    write(".nojekyll", "")


REDIRECT = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<title>{brand}</title>
<link rel="canonical" href="{to}">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url={to}">
<script>location.replace("{to}");</script>
</head>
<body><p>→ <a href="{to}">{to}</a></p></body>
</html>
"""


def build_redirects(posts, page_defs):
    """Страницы-заглушки по адресам, где сайт жил раньше.

    Без них смена языковой схемы превращает всё, что уже попало в индекс и в
    чужие закладки, в 404. Список старых префиксов — в config.LEGACY_PREFIXES.
    """
    paths = [""] + [p["slug"] for p in page_defs if p["slug"]]
    paths += ["blog/"] + [f"blog/{p['slug']}/" for p in posts]

    made = 0
    for old_prefix, new_prefix in cfg.LEGACY_PREFIXES.items():
        for path in paths:
            old = old_prefix + path
            # не затираем настоящую страницу, если старый адрес совпал с новым
            if old in {cfg.LANG_PREFIX[l] + p for l in cfg.LANGS for p in paths}:
                continue
            write(old + "index.html",
                  REDIRECT.format(lang=cfg.DEFAULT_LANG, brand=cfg.BRAND,
                                  to=f"{cfg.SITE}/{new_prefix}{path}"))
            made += 1
    return made


NOT_FOUND = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>404 — {brand}</title>
<meta name="robots" content="noindex, follow">
<link rel="icon" href="{favicon}">
<link rel="stylesheet" href="{site}/{assets}/{css_bundle}">
<script>{perf}</script>
<style>
  .nf{{max-width:720px; margin:0 auto; padding:22vh 24px 12vh; text-align:left;}}
  .nf__code{{font-family:var(--font-mono); font-size:13px; letter-spacing:.14em;
             color:var(--yellow); margin-bottom:18px;}}
  .nf h1{{font-size:clamp(38px,8vw,84px); line-height:1; margin-bottom:20px;}}
  .nf p{{font-size:17px; line-height:1.6; color:var(--g-text-2); margin-bottom:14px; max-width:52ch;}}
  .nf__en{{font-size:15px; color:var(--g-text-3);}}
  .nf__links{{display:flex; flex-wrap:wrap; gap:12px; margin-top:32px;}}
</style>
</head>
<body class="page-404">
<main class="nf" id="content">
  <p class="nf__code">ERROR 404</p>
  <h1>СТРАНИЦЫ НЕТ</h1>
  <p>Такого адреса на сайте не существует. Возможно, ссылка устарела или в ней опечатка.</p>
  <p class="nf__en">This page doesn't exist. The link is probably outdated or mistyped.</p>
  <div class="nf__links">
    <a class="btn btn--yellow" href="{site}/">НА ГЛАВНУЮ / HOME</a>
    <a class="btn btn--outline" href="{site}/blog/">БЛОГ / BLOG</a>
    <a class="btn btn--outline" href="{site}/services/">УСЛУГИ / SERVICES</a>
  </div>
</main>
</body>
</html>
"""


def build_404():
    """GitHub Pages отдаёт /404.html на любой неизвестный адрес.

    Пути здесь абсолютные: файл показывается по произвольному URL любой
    вложенности, и относительные ссылки на css из него не разрешаются.
    """
    from core.theme import ASSETS, FAVICON, PERF_SNIPPET
    write("404.html", NOT_FOUND.format(
        lang=cfg.DEFAULT_LANG, brand=cfg.BRAND, site=cfg.SITE,
        assets=cfg.ASSETS, favicon=FAVICON,
        css_bundle=ASSETS["css"], perf=PERF_SNIPPET))


# ---------------------------------------------------------------------------
# Уборка: всё, что не перечислено, было сгенерировано прошлой сборкой.
# Без этого смена схемы адресов оставляет мёртвые страницы, которые
# продолжают индексироваться.
# ---------------------------------------------------------------------------
KEEP = {"Tools", "content", "assets", "admin", "supabase",
        "README.md", ".git", ".gitignore", ".nojekyll", "CNAME"}


def clean():
    import shutil
    removed = 0
    for name in os.listdir(cfg.ROOT):
        if name in KEEP or name.startswith("."):
            continue
        full = os.path.join(cfg.ROOT, name)
        if os.path.isdir(full):
            shutil.rmtree(full)
        else:
            os.remove(full)
        removed += 1
    return removed


# ---------------------------------------------------------------------------
def main():
    posts = pages.load_posts()
    cases = pages.load_cases()
    page_defs = pages.load_pages()

    wiped = clean()

    built = assets.build()          # склейка CSS/JS до страниц: в них попадут имена бандлов
    set_assets(built)

    print(f"контент: {len(page_defs)} страниц, {len(cases)} кейсов, {len(posts)} статей")
    print(assets.report(built) + "\n")

    made = 0
    for lang in cfg.LANGS:
        for page in page_defs:
            ctx = Ctx(lang, page["slug"])
            out = pages.build_page(page, ctx, posts, cases)
            print(f"  {out}")
            made += 1

        blog.build_index(posts, lang)
        blog.build_feed(posts, lang)
        made += 2
        for post in posts:
            blog.build_post(post, posts, lang)
            made += 1

    n = build_sitemap(posts)
    build_robots()
    build_404()
    red = build_redirects(posts, page_defs)

    print(f"\n{made} файлов · sitemap: {n} URL · редиректов: {red} · очищено: {wiped}")
    print("\nвремя чтения статей:")
    for lang in cfg.LANGS:
        mins = [blog.read_minutes(p, lang) for p in posts]
        odd = [p["slug"] for p in posts if not 7 <= blog.read_minutes(p, lang) <= 15]
        print(f"  {lang}: {min(mins)}–{max(mins)} мин" + (f"  вне диапазона: {odd}" if odd else ""))


if __name__ == "__main__":
    main()
