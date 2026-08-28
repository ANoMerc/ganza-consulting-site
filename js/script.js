/* Ganza Consulting — shared UI behaviour.
 *
 * 1. RU/EN switch. On the landing page both languages live in the DOM
 *    (.lang-ru / .lang-en), so switching is instant and the URL is synced to
 *    the matching physical page (/ or /ru/) via replaceState — the address bar
 *    always shows a shareable, indexable URL. On blog pages the switch is a
 *    plain link to the mirrored article, so nothing here has to run.
 * 2. Mobile menu.
 * 3. Article extras: reading progress bar + active heading in the contents box.
 */
(function () {
  "use strict";

  var html = document.documentElement;
  var langSwitch = document.getElementById("langSwitch");
  var burger = document.getElementById("burger");
  var nav = document.getElementById("nav");
  var STORE_KEY = "ganza:lang";

  function store(key, value) {
    try { window.localStorage.setItem(key, value); } catch (e) { /* private mode */ }
  }

  // ---- language toggle -----------------------------------------------------
  function setLang(lang, syncUrl) {
    html.setAttribute("data-lang", lang);
    html.setAttribute("lang", lang);
    store(STORE_KEY, lang);

    if (syncUrl && langSwitch && window.history && window.history.replaceState) {
      var target = langSwitch.getAttribute("data-url-" + lang);
      if (target) {
        var url = new URL(target, window.location.href);
        url.hash = window.location.hash;
        window.history.replaceState(null, "", url.toString());
      }
    }
    document.dispatchEvent(new CustomEvent("ganza:lang", { detail: { lang: lang } }));
  }

  if (langSwitch) {
    langSwitch.addEventListener("click", function () {
      setLang(html.getAttribute("data-lang") === "ru" ? "en" : "ru", true);
    });
  }

  // ---- mobile nav ----------------------------------------------------------
  if (burger && nav) {
    burger.addEventListener("click", function () {
      nav.classList.toggle("is-open");
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
      });
    });
  }

  // ---- reading progress bar (article pages) --------------------------------
  var article = document.querySelector(".post__body");
  if (article) {
    var bar = document.createElement("div");
    bar.className = "read-progress";
    bar.innerHTML = '<span></span>';
    document.body.appendChild(bar);
    var fill = bar.firstChild;

    var update = function () {
      var rect = article.getBoundingClientRect();
      var total = rect.height - window.innerHeight;
      var done = total > 0 ? Math.min(1, Math.max(0, -rect.top / total)) : 0;
      fill.style.width = (done * 100).toFixed(1) + "%";
    };
    update();
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
  }

  // ---- table of contents: highlight the section being read -----------------
  var tocLinks = document.querySelectorAll(".post__toc a");
  if (tocLinks.length && "IntersectionObserver" in window) {
    var map = {};
    tocLinks.forEach(function (a) {
      var id = a.getAttribute("href").slice(1);
      var el = document.getElementById(id);
      if (el) map[id] = a;
    });
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        tocLinks.forEach(function (a) { a.classList.remove("is-current"); });
        var link = map[entry.target.id];
        if (link) link.classList.add("is-current");
      });
    }, { rootMargin: "-10% 0px -70% 0px" });
    Object.keys(map).forEach(function (id) {
      observer.observe(document.getElementById(id));
    });
  }

  // ---- blog index: filter by topic ----------------------------------------
  var filters = document.querySelectorAll(".blog-filter__btn");
  if (filters.length) {
    var cards = document.querySelectorAll(".post-card");
    filters.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var tag = btn.getAttribute("data-filter");
        filters.forEach(function (b) { b.classList.remove("is-active"); });
        btn.classList.add("is-active");
        cards.forEach(function (card) {
          var show = tag === "*" || card.getAttribute("data-tag") === tag;
          card.style.display = show ? "" : "none";
        });
      });
    });
  }
})();
