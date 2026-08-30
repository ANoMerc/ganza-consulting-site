# -*- coding: utf-8 -*-
"""ЯДРО · Блоки контента.

Контент в content/ описан списком кортежей ("тип", данные). Здесь они
превращаются в HTML. Один и тот же набор блоков используют и статьи блога,
и кейсы, и обычные страницы — поэтому новый тип блока появляется в одном
месте и сразу доступен везде.

Доступные типы:
    ("h2",  "Заголовок")            ("h3", "Подзаголовок")
    ("p",   "Абзац, можно <b>")     ("q",  "Врезка-цитата")
    ("ul",  ["пункт", ...])         ("ol", ["пункт", ...])
    ("checklist", ["пункт", ...])   ("note", "Жёлтая врезка")
    ("steps", [("Шаг", "текст"), ...])
    ("table", {"caption": ..., "head": [...], "rows": [[...], ...]})
"""
import re

from . import config as cfg

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
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")[:60] or "section"


def resolve(text, ctx):
    """Подстановки внутри контента: HOME, BLOG, CASES, SERVICES, PRIVACY, TAKE, TEMPLATES."""
    return (text.replace("{{HOME}}", ctx.to())
                .replace("{{BLOG}}", ctx.to("blog/"))
                .replace("{{CASES}}", ctx.to("cases/"))
                .replace("{{SERVICES}}", ctx.to("services/"))
                .replace("{{PRIVACY}}", ctx.to("privacy/"))
                .replace("{{TAKE}}", ctx.to("what-i-take/"))
                .replace("{{TEMPLATES}}", ctx.to("templates/")))


def plain(blocks):
    """Весь текст без разметки — для подсчёта времени чтения."""
    out = []
    for kind, content in blocks:
        if kind in ("ul", "ol", "checklist"):
            out.extend(content)
        elif kind == "steps":
            for t, b in content:
                out += [t, b]
        elif kind == "table":
            out.extend(content.get("head", []))
            for row in content.get("rows", []):
                out.extend(row)
            out.append(content.get("caption", ""))
        else:
            out.append(content)
    return " ".join(out)


def render(blocks, ctx, collect_toc=False):
    """Список блоков → HTML. Возвращает (html, оглавление)."""
    out, toc = [], []
    r = lambda s: resolve(s, ctx)

    for kind, content in blocks:
        if kind == "h2":
            a = anchor(content)
            toc.append((a, re.sub(r"<[^>]+>", "", content)))
            out.append(f'<h2 id="{a}" data-reveal>{r(content)}</h2>')
        elif kind == "h3":
            out.append(f'<h3 id="{anchor(content)}" data-reveal>{r(content)}</h3>')
        elif kind == "p":
            out.append(f"<p data-reveal>{r(content)}</p>")
        elif kind in ("ul", "ol"):
            items = "".join(f"<li>{r(li)}</li>" for li in content)
            out.append(f"<{kind} data-reveal>{items}</{kind}>")
        elif kind == "checklist":
            items = "".join(f"<li>{r(li)}</li>" for li in content)
            out.append(f'<ul class="post__checklist" data-reveal>{items}</ul>')
        elif kind == "q":
            out.append(f'<blockquote class="post__pull" data-reveal>{r(content)}</blockquote>')
        elif kind == "note":
            out.append(f'<div class="post__note" data-reveal>{r(content)}</div>')
        elif kind == "steps":
            lis = "".join(f"<li><strong>{r(t)}</strong><span>{r(b)}</span></li>"
                          for t, b in content)
            out.append(f'<ol class="post__steps" data-reveal>{lis}</ol>')
        elif kind == "table":
            # Таблица-паспорт («ключ — значение») шапки не имеет. Пустой <thead>
            # рисовал бы поперёк неё серую полосу, поэтому если все заголовки
            # пустые, шапку не выводим вовсе.
            heads = content.get("head") or []
            has_head = any(str(h).strip() for h in heads)
            thead = ""
            if has_head:
                cells = "".join(f'<th scope="col">{h}</th>' for h in heads)
                thead = f"<thead><tr>{cells}</tr></thead>"
            rows = "".join("<tr>" + "".join(f"<td>{r(c)}</td>" for c in row) + "</tr>"
                           for row in content["rows"])
            cap = f'<caption>{content["caption"]}</caption>' if content.get("caption") else ""
            cls = "post__table" + ("" if has_head else " post__table--plain")
            out.append('<div class="post__table-wrap" data-reveal>'
                       f'<table class="{cls}">{cap}{thead}<tbody>{rows}</tbody></table></div>')
        else:
            raise ValueError(f"неизвестный тип блока: {kind!r}")

    html = "\n        ".join(out)
    return (html, toc) if collect_toc else html


def read_minutes(blocks, lang, extra=""):
    from .theme import count_words
    return max(2, round(count_words(plain(blocks) + " " + extra) / cfg.WPM[lang]))
