#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerates sitemap.xml (with hreflang pairs) and robots.txt.

Run after build_site.py / build_blog.py:  python3 build_sitemap.py
"""
import datetime

from buildlib import SITE, write
from build_blog import load_posts

TODAY = datetime.date.today().isoformat()


def url_entry(en, ru, lastmod, priority, changefreq):
    out = []
    for loc, other in ((en, ru), (ru, en)):
        out.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
    <xhtml:link rel="alternate" hreflang="en" href="{en}"/>
    <xhtml:link rel="alternate" hreflang="ru" href="{ru}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{en}"/>
  </url>""")
    return out


def main():
    posts = load_posts()
    entries = []
    entries += url_entry(f"{SITE}/", f"{SITE}/ru/", TODAY, "1.0", "weekly")
    entries += url_entry(f"{SITE}/blog/", f"{SITE}/ru/blog/", TODAY, "0.9", "weekly")
    for post in sorted(posts, key=lambda p: p["date"], reverse=True):
        entries += url_entry(
            f"{SITE}/blog/{post['slug']}/",
            f"{SITE}/ru/blog/{post['slug']}/",
            post["updated"], "0.8", "monthly",
        )

    xml = ("""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
"""
           + "\n".join(entries)
           + "\n</urlset>\n")
    write("sitemap.xml", xml)

    robots = f"""User-agent: *
Allow: /
Disallow: /admin/
Disallow: /_src/
Disallow: /en/

Sitemap: {SITE}/sitemap.xml
"""
    write("robots.txt", robots)
    write(".nojekyll", "")
    print(f"wrote sitemap.xml ({len(entries)} urls), robots.txt, .nojekyll")


if __name__ == "__main__":
    main()
