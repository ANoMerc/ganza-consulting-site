# -*- coding: utf-8 -*-
"""ЯДРО · Оболочка страницы.

<head>, шапка, подвал, JSON-LD и вычисление относительных путей. Всё, что
одинаково на каждой странице сайта. Меняется редко; когда меняется —
меняется сразу везде.
"""
import html as html_mod
import json
import os
import re

from . import config as cfg

esc = html_mod.escape


# ---------------------------------------------------------------------------
# Ctx — «где я нахожусь». Из него берутся все относительные пути.
# ---------------------------------------------------------------------------
class Ctx:
    """Контекст одной страницы: язык и её адрес относительно корня сайта."""

    def __init__(self, lang, path=""):
        self.lang = lang
        self.path = path                      # 'services/', 'blog/slug/', '' для главной
        self.L = cfg.LABELS[lang]
        self.prefix = cfg.LANG_PREFIX[lang]   # '' или 'ru/'
        self.url_path = self.prefix + path    # адрес от корня сайта
        self.depth = len([s for s in self.url_path.split("/") if s])

    # --- пути -------------------------------------------------------------
    @property
    def up(self):
        """До корня сайта."""
        return "../" * self.depth or "./"

    @property
    def asset(self):
        """До папки assets/."""
        return ("../" * self.depth) + cfg.ASSETS + "/"

    def to(self, path=""):
        """Ссылка на другую страницу того же языка."""
        target = cfg.LANG_PREFIX[self.lang] + path
        return ("../" * self.depth) + target or "./"

    def alt(self, lang):
        """Тот же документ на другом языке."""
        target = cfg.LANG_PREFIX[lang] + self.path
        return ("../" * self.depth) + target or "./"

    def abs(self, path=None, lang=None):
        """Абсолютный URL — для canonical, hreflang, JSON-LD, sitemap."""
        lang = lang or self.lang
        path = self.path if path is None else path
        return f"{cfg.SITE}/{cfg.LANG_PREFIX[lang]}{path}"


# ---------------------------------------------------------------------------
# Мелочи
# ---------------------------------------------------------------------------
def fmt_date(iso, lang):
    y, m, d = iso.split("-")
    if lang == "ru":
        return f"{int(d)} {cfg.MONTHS['ru'][int(m) - 1]} {y}"
    return f"{cfg.MONTHS['en'][int(m) - 1]} {int(d)}, {y}"


def count_words(s):
    return len(re.findall(r"[\w'’-]+", re.sub(r"<[^>]+>", " ", s), flags=re.UNICODE))


def write(path, content):
    full = os.path.join(cfg.ROOT, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# <head>
# ---------------------------------------------------------------------------
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
           "%3Crect width='100' height='100' rx='22' fill='%230b0b09'/%3E%3Ctext x='50' y='73' "
           "font-size='66' font-family='Arial Black,sans-serif' font-weight='900' fill='%23e8ff2e' "
           "text-anchor='middle'%3EG%3C/text%3E%3C/svg%3E")

FONTS = ("https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Mono:wght@400;700"
         "&family=Inter:wght@400;500;600;700&display=swap")


def head(ctx, *, title, description, keywords="", og_image=None, og_image_alt="",
         og_type="website", jsonld="", extra_meta="", robots=None, body_class="",
         feed=None):
    robots = robots or "index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1"
    og_image = og_image or f"{cfg.SITE}/{cfg.ASSETS}/img/og-cover.png"

    alts = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{ctx.abs(lang=l)}">' for l in cfg.LANGS
    )
    feed_link = (f'\n<link rel="alternate" type="application/rss+xml" '
                 f'title="{esc(cfg.BRAND)} — {ctx.L["blog"]}" href="{feed}">' if feed else "")
    locale = {"en": "en_US", "ru": "ru_RU"}
    alt_locale = [locale[l] for l in cfg.LANGS if l != ctx.lang]

    return f"""<!DOCTYPE html>
<html lang="{ctx.lang}" data-lang="{ctx.lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
{f'<meta name="keywords" content="{keywords}">' if keywords else ''}
<meta name="author" content="{esc(cfg.AUTHOR_NAME)}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#0b0b09">
<link rel="canonical" href="{ctx.abs()}">
{alts}
<link rel="alternate" hreflang="x-default" href="{ctx.abs(lang=cfg.DEFAULT_LANG)}">{feed_link}

<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(cfg.BRAND)}">
<meta property="og:locale" content="{locale[ctx.lang]}">
{chr(10).join(f'<meta property="og:locale:alternate" content="{a}">' for a in alt_locale)}
<meta property="og:url" content="{ctx.abs()}">
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
<link rel="stylesheet" href="{ctx.asset}css/base.css">
<link rel="stylesheet" href="{ctx.asset}css/builder.css">
<link rel="stylesheet" href="{ctx.asset}css/blog.css">
<link rel="stylesheet" href="{ctx.asset}css/glass.css">
{jsonld}<script src="{ctx.asset}js/analytics.js" defer></script>
</head>
<body class="{body_class}">
"""


# ---------------------------------------------------------------------------
# JSON-LD
# ---------------------------------------------------------------------------
def org_node():
    return {
        "@type": "Organization", "@id": f"{cfg.SITE}/#organization",
        "name": cfg.BRAND, "url": f"{cfg.SITE}/", "email": cfg.EMAIL,
        "logo": {"@type": "ImageObject", "url": f"{cfg.SITE}/{cfg.ASSETS}/img/og-cover.png",
                 "width": 1200, "height": 630},
        "sameAs": [cfg.TELEGRAM, cfg.LINKEDIN],
    }


def person_node(lang):
    return {
        "@type": "Person", "@id": f"{cfg.SITE}/#george-mercer",
        "name": cfg.AUTHOR_NAME,
        "url": f"{cfg.SITE}/{cfg.LANG_PREFIX[lang]}#about",
        "image": f"{cfg.SITE}/{cfg.ASSETS}/img/founder.jpg",
        "description": cfg.AUTHOR_BIO[lang],
        "jobTitle": "Independent consultant" if lang == "en" else "Независимый консультант",
        "worksFor": {"@id": f"{cfg.SITE}/#organization"},
        "sameAs": [cfg.TELEGRAM, cfg.LINKEDIN],
    }


def jsonld(graph):
    return ('<script type="application/ld+json">\n'
            + json.dumps({"@context": "https://schema.org", "@graph": graph},
                         ensure_ascii=False, indent=2) + "\n</script>\n")


# ---------------------------------------------------------------------------
# Шапка / подвал
# ---------------------------------------------------------------------------
def ticker(ctx):
    return f"""<div class="ticker" aria-hidden="true">
  <div class="ticker__track"><span>{ctx.L['ticker'] * 2}</span></div>
</div>
"""


def header(ctx, active=""):
    L = ctx.L
    links = []
    for item in cfg.NAV:
        href = ctx.to(item["page"]) + ("#" + item["anchor"] if item.get("anchor") else "")
        cls = ' class="is-active"' if active and active == item["key"] else ""
        links.append(f'      <a href="{href}"{cls}>{L[item["key"]]}</a>')

    other = [l for l in cfg.LANGS if l != ctx.lang][0]
    opts = "".join(
        f'<span class="lang-switch__opt{" is-active" if l == ctx.lang else ""}">{l.upper()}</span>'
        + ('<span class="lang-switch__sep">/</span>' if l != cfg.LANGS[-1] else "")
        for l in cfg.LANGS
    )

    return f"""<header class="site-header" id="top">
  <div class="site-header__inner">
    <a href="{ctx.to()}" class="logo" data-track="logo">
      <span class="logo__mark">G</span>
      <span class="logo__text">GANZA<br>CONSULTING</span>
    </a>

    <nav class="nav" id="nav" aria-label="{'Основная навигация' if ctx.lang == 'ru' else 'Main navigation'}">
{chr(10).join(links)}
    </nav>

    <div class="header-actions">
      <a class="lang-switch" href="{ctx.alt(other)}" hreflang="{other}"
         aria-label="{'Сменить язык' if ctx.lang == 'ru' else 'Switch language'}" data-track="lang-switch">{opts}</a>
      <a class="btn btn--small btn--yellow" href="{cfg.TELEGRAM}" target="_blank" rel="noopener" data-track="header-telegram">{L['telegram']}</a>
      <button class="burger" id="burger" aria-label="{L['menu']}" type="button">{L['menu']}</button>
    </div>
  </div>
</header>
"""


def footer(ctx, scripts=()):
    L = ctx.L
    extra = "".join(f'<script src="{ctx.asset}js/{s}" defer></script>\n' for s in scripts)
    return f"""
<footer class="footer" id="contact">
  <div class="footer__top">
    <h2>{L['footer_h']}</h2>
    <div class="footer__contacts">
      <a class="contact-link" href="{cfg.TELEGRAM}" target="_blank" rel="noopener" data-track="footer-telegram">
        <span class="contact-link__label">TELEGRAM</span>
        <span class="contact-link__value">@groovebliss ↗</span>
      </a>
      <a class="contact-link" href="{cfg.LINKEDIN}" target="_blank" rel="noopener" data-track="footer-linkedin">
        <span class="contact-link__label">LINKEDIN</span>
        <span class="contact-link__value">george-mercer ↗</span>
      </a>
      <a class="contact-link" href="mailto:{cfg.EMAIL}" data-track="footer-email">
        <span class="contact-link__label">EMAIL</span>
        <span class="contact-link__value">{cfg.EMAIL} ↗</span>
      </a>
    </div>
  </div>

  <div class="footer__bottom">
    <p class="footer__joke">{L['footer_joke']}</p>
    <p class="footer__legal">{L['footer_legal']}</p>
  </div>
</footer>

<script src="{ctx.asset}js/site.js" defer></script>
{extra}</body>
</html>
"""
