#!/usr/bin/env python3
"""Generates /blog/index.html and /blog/<slug>/index.html from POSTS below.
Run: python3 build_blog.py
"""
import os, re, math, json, html as html_mod

esc = html_mod.escape

SITE = "https://anomerc.github.io/ganza-consulting-site"
ROOT = os.path.dirname(os.path.abspath(__file__))

POSTS = [
    dict(
        slug="infrastructure-inbreeding",
        date="2026-06-02",
        tag="Leadership",
        title="Infrastructure Inbreeding: Why Promoting Only From Within Puts Your Company at Risk",
        dek="Universities have a name for hiring only their own graduates. Most companies have the same problem — they just don't have a name for it.",
        description="Why closed internal talent pipelines quietly erode a company's ability to adapt — and where the line is between healthy internal promotion and organizational inbreeding.",
        body=[
            ("p", "Universities have a name for hiring almost exclusively their own graduates: <strong>academic inbreeding</strong>. Less diversity of ideas, more replication of the same approach, slow intellectual isolation."),
            ("p", "Companies have the same pattern. They just don't have a name for it."),
            ("p", "Promoting from within isn't the problem — it protects culture and speeds up onboarding. The problem starts when the pipeline closes almost entirely: when most executives walked the same path, sat in the same rooms, absorbed the same management philosophy."),
            ("p", "What that produces, reliably:"),
            ("ul", [
                "New ideas read as threats to \"how we do things here.\"",
                "Groupthink gets easier — nobody in the room has a genuinely different reference point.",
                "The organization gets slower to notice market shifts.",
                "Internal politics start outweighing internal logic.",
                "Outside candidates are filed as \"won't fit,\" regardless of what they bring.",
            ]),
            ("p", "The strange part: these companies often look stable from the outside. Processes run smoothly. Everyone speaks the same language. Meetings are calm."),
            ("p", "That calm is exactly what hides it. The system isn't adapting to its environment anymore — it's reproducing itself."),
            ("q", "Where's the line between developing internal talent and building infrastructure inbreeding — a system that gradually loses its ability to learn?"),
            ("p", "What's the right ratio, in your experience — internal promotions vs. external hires at the leadership level?"),
        ],
        hashtags=["OrganizationalDesign", "Leadership", "CorporateCulture", "TalentStrategy", "ExecutiveHiring"],
    ),
    dict(
        slug="lidl-digital-transformation-failure",
        date="2026-06-16",
        tag="Case Study",
        title="How Lidl Lost €500 Million: A Case Study in Digital Transformation Failure",
        dek="Lidl's eLWIS project didn't fail in a single moment. It drifted — until keeping it alive cost more than admitting it was dead.",
        description="A breakdown of Lidl's failed SAP rollout: how customizing a system instead of adapting processes, and a widening gap between reports and reality, cost the company roughly €500 million.",
        body=[
            ("p", "In 2011, Lidl started eLWIS — a SAP-based system meant to unify operations across 30 countries. Simple goal, huge scope."),
            ("p", "In 2018, they shut it down. Cost: roughly <strong>€500 million</strong>. They rolled back to the old in-house system."),
            ("p", "What actually happened inside:"),
            ("p", "Lidl customized SAP to match its existing processes instead of adapting processes to SAP's standard. Every customization added complexity. Every added complexity got labeled \"solvable\" — because on paper, it was."),
            ("p", "Meanwhile, reporting still looked fine. External metrics stayed acceptable. The gap between what dashboards showed and what engineers actually saw kept widening, quietly."),
            ("p", "Engineers flagged scalability and architecture risk. Those signals either didn't reach the people who could act on them, or got diluted somewhere between layers of \"let's not escalate this yet.\""),
            ("p", "The project didn't fail in a moment. It drifted — until keeping it alive cost more than admitting it was dead."),
            ("p", "Large transformations rarely break from one bad decision. They break from the accumulated gap between what's actually happening and what people feel safe saying out loud."),
            ("q", "If your team could tell you the real state of a project without it costing them anything — would today's numbers still look the same?"),
        ],
        hashtags=["DigitalTransformation", "ProjectManagement", "ChangeManagement", "ERP", "RiskManagement"],
    ),
    dict(
        slug="why-startups-need-consulting",
        date="2026-06-30",
        tag="Startups",
        title="Why Startups Need Consulting (Even the Ones That Think They Can't Afford It)",
        dek="Consulting isn't for companies big enough to afford being slow. It's most useful exactly when you're too small to afford being wrong.",
        description="Why the founders who avoid consulting usually aren't avoiding the cost — and what a startup should actually look for in an outside opinion.",
        body=[
            ("p", "Most founders think consulting is for companies big enough to afford being slow."),
            ("p", "It's actually the opposite. Consulting is most useful exactly when you're too small to afford being wrong."),
            ("p", "A 200-person company can absorb a bad six-month bet on the wrong process, the wrong automation, the wrong hire. A 6-person startup can't — one wrong call burns a quarter of runway you don't get back."),
            ("p", "What a startup actually needs from a consultant isn't a strategy deck. It's someone who's seen the specific failure mode you're about to walk into, and can tell you before it costs you three months."),
            ("p", "The founders who avoid consulting usually aren't avoiding the cost. They're avoiding the idea that someone outside the company might see the problem faster than they can. That instinct is understandable — and it's the expensive one."),
            ("p", "The founders who use consulting well don't outsource decisions. They buy a second, sharper pair of eyes for the one decision that's too important to get wrong on the first try."),
            ("p", "You don't need a retainer. You need someone for the one hard question, at the one moment it actually matters."),
            ("q", "What's the one decision in your startup right now where you'd genuinely want an outside opinion before committing?"),
        ],
        hashtags=["StartupAdvice", "Founders", "BusinessConsulting", "Entrepreneurship", "StartupGrowth"],
    ),
    dict(
        slug="audit-nobody-reads",
        date="2026-07-14",
        tag="Consulting",
        title="The Audit Nobody Reads: Why Most Business Audits Fail to Drive Change",
        dek="Most audits are built to demonstrate thoroughness, not to be acted on. That's a design problem, not an accuracy problem.",
        description="Why most business audits end up as a PDF opened once — and what a business audit needs to look like to actually change what happens on Monday morning.",
        body=[
            ("p", "Most business audits end the same way: a 60-slide deck, a round of applause in the final meeting, and a PDF that gets opened once — the day it's delivered."),
            ("p", "Nobody's lying in that meeting. The findings are usually correct. The problem isn't accuracy. It's design."),
            ("p", "Most audits are built to demonstrate thoroughness, not to be acted on. They cover every department, every risk, every possible finding — because \"comprehensive\" is what gets sold and what looks defensible later. The output is a document you can point to, not a decision you can make."),
            ("p", "An audit that actually gets used looks different. It picks one real, specific, expensive problem — not twelve medium ones — and it ends with an answer, not a menu of \"options to consider.\""),
            ("p", "If you can't tell, from the last page, exactly what to do on Monday morning, the audit did its job for the consultant, not for you."),
            ("q", "Next time someone hands you an audit — count how many of the findings actually have an owner and a deadline attached. That number tells you more than the deck does."),
        ],
        hashtags=["BusinessConsulting", "ProcessImprovement", "Audit", "OperationalExcellence", "ManagementConsulting"],
    ),
    dict(
        slug="one-person-consulting-studio",
        date="2026-07-21",
        tag="Consulting",
        title="The One-Person Consulting Studio Advantage: Why Small Beats Big",
        dek="\"What if you get sick?\" is the most common objection to hiring a solo consultant. It's usually asked backwards.",
        description="Why diluted accountability, not team size, is the real risk in consulting — and what you actually get from working with a one-person studio instead of an agency.",
        body=[
            ("p", "\"What if you get sick?\" is the most common objection to hiring a solo consultant instead of an agency."),
            ("p", "It's a fair question. It's also usually asked backwards."),
            ("p", "At a large agency, the person who sold you the project and the person doing the work are rarely the same person. By the time your problem reaches someone senior enough to actually solve it, it's passed through two account managers and a kickoff deck. If that senior person leaves, you often don't know — the agency just quietly reassigns."),
            ("p", "At a one-person studio, there's no one to hide behind. The person on the call is the person doing the work, which means there's nowhere for a wrong assumption to survive unnoticed. It also means you can only take on a handful of clients at once — which sounds like a limitation until you realize it's the only way anyone can promise you their full attention instead of 20% of it."),
            ("p", "Small isn't the risk. Diluted accountability is the risk. Small is just where accountability has nowhere left to hide."),
            ("q", "Would you rather have 20% of a senior person's attention, or 100% of someone slightly less famous?"),
        ],
        hashtags=["Consulting", "BoutiqueConsulting", "SmallBusiness", "ClientExperience", "Freelance"],
    ),
    dict(
        slug="when-not-to-automate",
        date="2026-08-04",
        tag="Automation & AI",
        title="When Not to Automate: The Hidden Risk of Automating Broken Processes",
        dek="Automating a broken process doesn't fix it. It makes the broken version run faster, more consistently, and harder to notice.",
        description="Why the right question before any automation project isn't \"can this be automated\" — it's whether the process deserves to survive in its current form at all.",
        body=[
            ("p", "Every automation pitch sounds the same: \"we'll save you X hours a week.\" Almost none of them ask whether the process being automated should still exist."),
            ("p", "Automating a broken process doesn't fix it. It just makes the broken version run faster, more consistently, and harder to notice — because now nobody has to manually suffer through it to see how bad it is."),
            ("p", "We once evaluated replacing a full-time hire with an AI manager for handling estimates, documents, and logistics. The honest answer wasn't \"yes, automate it.\" It was: most of the risk wasn't in the manual work — it was in a handful of judgment calls that shouldn't be automated at all. So we automated the 80% that was pure repetition, and left the 20% that actually needed a human decision exactly where it was."),
            ("p", "The question worth asking before any automation project isn't \"can this be automated.\" It's \"does this process deserve to survive in its current form at all.\""),
            ("q", "If you automated your worst process tomorrow exactly as it exists today — would you be proud of what you shipped?"),
        ],
        hashtags=["Automation", "AI", "ProcessOptimization", "DigitalTransformation", "Efficiency"],
    ),
    dict(
        slug="multilingual-website-not-converting",
        date="2026-08-13",
        tag="Web Development",
        title="Why Your Multilingual Website Isn't Converting (It's Not About Translation)",
        dek="Translation is the easy 20% of localization. The 80% that determines whether a site converts has nothing to do with words.",
        description="What actually makes a multi-market website convert — beyond translation: layout direction, reading patterns, and local trust signals that word-for-word translation gets wrong.",
        body=[
            ("p", "Most companies localize a website by translating it. That's the easy 20% of the problem, and it's the part everyone gets right."),
            ("p", "The 80% that actually determines whether a multilingual site converts has nothing to do with translation: right-to-left layout that doesn't quietly break your grid, alphabet and reading-direction differences that change how people scan a page, and local specifics — payment habits, trust signals, even color associations — that a word-for-word translation carries over by accident, wrong."),
            ("p", "A site that reads correctly but \"feels\" imported rarely converts. Visitors can't always say why it feels off. They just leave faster."),
            ("p", "The test isn't \"does it read correctly in this language.\" It's \"would someone who only reads this language assume it was built by someone who only reads this language.\""),
            ("q", "If you translated your site tomorrow into a language with a different alphabet or reading direction — would it still look designed, or just translated?"),
        ],
        hashtags=["WebDevelopment", "Localization", "InternationalBusiness", "UXDesign", "GlobalMarketing"],
    ),
    dict(
        slug="consulting-retainer-trap",
        date="2026-08-25",
        tag="Consulting",
        title="The Consulting Retainer Trap: Why Monthly Retainers Rarely Solve Real Problems",
        dek="A retainer guarantees the consultant gets paid every month. It doesn't guarantee you get a hard problem solved.",
        description="Why most consulting retainers quietly turn into a subscription for activity instead of results — and what to ask before renewing one.",
        body=[
            ("p", "Most consulting relationships start with a retainer, because retainers are easier to sell than results."),
            ("p", "A retainer guarantees the consultant gets paid every month. It doesn't guarantee you get a hard problem solved — it guarantees you get <strong>something</strong> delivered every month, whether or not that's what actually moves the number you care about."),
            ("p", "That's how six-month retainers turn into eighteen-month retainers with a slide deck's worth of \"progress\" and no single decision anyone can point to as the reason things got better."),
            ("p", "The alternative isn't \"no consulting.\" It's consulting scoped to one specific, expensive problem, with a defined end — not a subscription to someone's calendar."),
            ("p", "If you can't name the one decision your current consulting engagement is supposed to produce, that's usually the real finding."),
            ("q", "Before renewing any retainer, ask one question out loud: what's the single decision this made possible that wouldn't have happened otherwise?"),
        ],
        hashtags=["Consulting", "ManagementConsulting", "BusinessStrategy", "ClientRelationships", "ConsultingIndustry"],
    ),
]


def word_count(post):
    n = 0
    for kind, content in post["body"]:
        if kind == "ul":
            n += sum(len(re.findall(r"\w+", li)) for li in content)
        else:
            n += len(re.findall(r"\w+", content))
    n += len(re.findall(r"\w+", post["title"])) + len(re.findall(r"\w+", post["dek"]))
    return n


def read_minutes(post):
    return max(2, math.ceil(word_count(post) / 200))


def body_html(post):
    parts = []
    for kind, content in post["body"]:
        if kind == "p":
            parts.append(f"<p>{content}</p>")
        elif kind == "ul":
            items = "".join(f"<li>{li}</li>" for li in content)
            parts.append(f"<ul>{items}</ul>")
        elif kind == "q":
            parts.append(f'<p class="post__question">{content}</p>')
    return "\n        ".join(parts)


def fmt_date_human(iso):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    y, m, d = iso.split("-")
    return f"{months[int(m)-1]} {int(d)}, {y}"


HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">

<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Ganza Consulting">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">

<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%230d0d0a'/%3E%3Ctext x='50' y='72' font-size='68' font-family='Arial Black,sans-serif' font-weight='900' fill='%23e8ff2e' text-anchor='middle'%3EG%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Mono:wght@400;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}css/style.css">
<link rel="stylesheet" href="{p}css/builder.css">
<link rel="stylesheet" href="{p}css/blog.css">
{jsonld}</head>
<body>

<div class="ticker" aria-hidden="true">
  <div class="ticker__track">
    <span>NOW BOOKING Q4 2026&nbsp;&nbsp;—&nbsp;&nbsp;CONSULTING + AUTOMATION + PROJECT MANAGEMENT&nbsp;&nbsp;—&nbsp;&nbsp;NO TEMPLATES&nbsp;&nbsp;—&nbsp;&nbsp;NOW BOOKING Q4 2026&nbsp;&nbsp;—&nbsp;&nbsp;CONSULTING + AUTOMATION + PROJECT MANAGEMENT&nbsp;&nbsp;—&nbsp;&nbsp;NO TEMPLATES&nbsp;&nbsp;—&nbsp;&nbsp;</span>
  </div>
</div>

<header class="site-header" id="top">
  <div class="site-header__inner">
    <a href="{p}en/index.html" class="logo">
      <span class="logo__mark">G</span>
      <span class="logo__text">GANZA<br>CONSULTING</span>
    </a>

    <nav class="nav" id="nav">
      <a href="{p}en/index.html#services">Services</a>
      <a href="{p}en/index.html#cases">Cases</a>
      <a href="{p}en/index.html#pricing">Pricing</a>
      <a href="{blogroot}">Blog</a>
      <a href="{p}en/index.html#contact">Contact</a>
    </nav>

    <div class="header-actions">
      <a class="btn btn--small btn--yellow" href="https://t.me/groovebliss" target="_blank" rel="noopener">TELEGRAM ↗</a>
      <button class="burger" id="burger" aria-label="Menu" type="button">MENU</button>
    </div>
  </div>
</header>
"""

FOOTER = """
<footer class="footer" id="contact">
  <div class="footer__top">
    <h2>READY TO SORT<br>OUT THE CHAOS?<br>WRITE TO US.</h2>
    <div class="footer__contacts">
      <a class="contact-link" href="https://t.me/groovebliss" target="_blank" rel="noopener">
        <span class="contact-link__label">TELEGRAM</span>
        <span class="contact-link__value">@groovebliss ↗</span>
      </a>
      <a class="contact-link" href="https://www.linkedin.com/in/george-mercer-55520b388/" target="_blank" rel="noopener">
        <span class="contact-link__label">LINKEDIN</span>
        <span class="contact-link__value">george-mercer ↗</span>
      </a>
      <a class="contact-link" href="mailto:onegeorgemercer@gmail.com">
        <span class="contact-link__label">EMAIL</span>
        <span class="contact-link__value">onegeorgemercer@gmail.com ↗</span>
      </a>
    </div>
  </div>

  <div class="footer__bottom">
    <p class="footer__joke">COPYRIGHT IS BORING</p>
    <p class="footer__legal">© 2026 GANZA CONSULTING. ALL RIGHTS... WHATEVER.</p>
  </div>
</footer>

<script src="{p}js/script.js"></script>
</body>
</html>
"""


def make_head(title, description, canonical, og_image, jsonld, p, blogroot, og_type="website"):
    return HEAD.format(title=title, description=description, canonical=canonical,
                        og_image=og_image, jsonld=jsonld, p=p, blogroot=blogroot, og_type=og_type)


# ---------------------------------------------------------------------------
# BLOG INDEX
# ---------------------------------------------------------------------------
def build_index():
    p = "../"
    ordered = list(reversed(POSTS))  # newest first
    cards = []
    for post in ordered:
        cards.append(f"""    <a class="post-card" href="{post['slug']}/">
      <div class="post-card__meta">
        <span class="post-card__tag">{esc(post['tag'])}</span>
        <span>{read_minutes(post)} min read · {fmt_date_human(post['date'])}</span>
      </div>
      <h2>{esc(post['title'])}</h2>
      <p class="post-card__excerpt">{esc(post['dek'])}</p>
      <span class="post-card__cta">READ THE ARTICLE →</span>
    </a>""")

    jsonld = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "Ganza Consulting — Blog",
  "url": "{SITE}/blog/",
  "publisher": {{
    "@type": "Organization",
    "name": "Ganza Consulting"
  }}
}}
</script>
"""

    html = make_head(
        title=esc("Blog — Ganza Consulting | Notes on Consulting, Automation & Hard Problems"),
        description=esc("Straight-talk essays on consulting, automation, project management and web development — no fluff, real cases, written by the person doing the work."),
        canonical=f"{SITE}/blog/",
        og_image=f"{SITE}/img/og-cover.png",
        jsonld=jsonld,
        p=p,
        blogroot="./",
    )
    html += f"""
<section class="blog-hero">
  <span class="tag tag--blue">BLOG</span>
  <h1>NOTES ON HARD PROBLEMS</h1>
  <p class="blog-hero__intro">Consulting, automation, project management, web development — written by the person who actually does the work. No listicles, no recycled frameworks.</p>
</section>

<section class="blog__grid">
{chr(10).join(cards)}
</section>
"""
    html += FOOTER.format(p=p)
    with open(os.path.join(ROOT, "blog", "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote blog/index.html")


# ---------------------------------------------------------------------------
# POST PAGES
# ---------------------------------------------------------------------------
def build_posts():
    for i, post in enumerate(POSTS):
        p = "../../"
        canonical = f"{SITE}/blog/{post['slug']}/"
        og_image = f"{SITE}/img/blog/{post['slug']}-cover.png"

        jsonld = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": {json.dumps(post['title'])},
  "description": {json.dumps(post['description'])},
  "image": "{og_image}",
  "datePublished": "{post['date']}",
  "dateModified": "{post['date']}",
  "author": {{
    "@type": "Person",
    "name": "George Mercer",
    "url": "{SITE}/en/index.html#about"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Ganza Consulting",
    "logo": {{
      "@type": "ImageObject",
      "url": "{SITE}/img/og-cover.png"
    }}
  }},
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "{canonical}"
  }}
}}
</script>
"""

        html = make_head(
            title=esc(f"{post['title']} | Ganza Consulting"),
            description=esc(post["description"]),
            canonical=canonical,
            og_image=og_image,
            jsonld=jsonld,
            p=p,
            blogroot="../",
            og_type="article",
        )

        prev_post = POSTS[i - 1] if i > 0 else POSTS[-1]
        next_post = POSTS[i + 1] if i < len(POSTS) - 1 else POSTS[0]

        tags_html = "".join(f'<span class="badge">#{h}</span>' for h in post["hashtags"])

        html += f"""
<article class="post">
  <a class="post__back" href="../">← ALL ARTICLES</a>
  <div class="post__head">
    <div class="post__meta">
      <span class="post__tag">{esc(post['tag'])}</span>
      <span>{read_minutes(post)} min read · {fmt_date_human(post['date'])}</span>
    </div>
    <h1>{esc(post['title'])}</h1>
    <p class="post__dek">{esc(post['dek'])}</p>
  </div>

  <div class="post__body">
        {body_html(post)}
  </div>

  <div class="post__tags">{tags_html}</div>

  <div class="post__cta">
    <div class="post__cta-box">
      <p>Have a problem like this one? We take on the single hard cases other consultants pass on.</p>
      <a class="btn btn--yellow" href="https://t.me/groovebliss" target="_blank" rel="noopener">MESSAGE ON TELEGRAM →</a>
      <a class="btn btn--outline" href="{p}en/index.html#pricing">SEE PRICING</a>
    </div>
  </div>
</article>

<nav class="post__nav">
  <a class="post__nav-link" href="../{prev_post['slug']}/">
    <span class="post__nav-label">← PREVIOUS</span>
    <span class="post__nav-title">{esc(prev_post['title'])}</span>
  </a>
  <a class="post__nav-link" href="../{next_post['slug']}/">
    <span class="post__nav-label">NEXT →</span>
    <span class="post__nav-title">{esc(next_post['title'])}</span>
  </a>
</nav>
"""
        html += FOOTER.format(p=p)

        post_dir = os.path.join(ROOT, "blog", post["slug"])
        os.makedirs(post_dir, exist_ok=True)
        with open(os.path.join(post_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote blog/{}/index.html — {} min read".format(post["slug"], read_minutes(post)))


if __name__ == "__main__":
    build_index()
    build_posts()
