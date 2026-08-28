/* ==========================================================================
   Ganza Consulting — поведение интерфейса.
   Ничего тяжёлого: наблюдатели пересечения вместо обработчиков скролла,
   всё выключается при prefers-reduced-motion.
   ========================================================================== */
(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* --- 1. Появление блоков при подходе к ним ------------------------------
     Элементы с [data-reveal] скрыты до тех пор, пока не приблизятся к экрану.
     Наблюдатель отключается сразу после показа — ничего не висит в памяти. */
  var revealables = document.querySelectorAll("[data-reveal]");
  if (revealables.length) {
    if (reduced || !("IntersectionObserver" in window)) {
      revealables.forEach(function (el) { el.classList.add("is-in"); });
    } else {
      document.documentElement.classList.add("has-reveal");
      var io = new IntersectionObserver(function (entries, obs) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add("is-in");
          obs.unobserve(e.target);
        });
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
      revealables.forEach(function (el) { io.observe(el); });
    }
  }

  /* --- 2. Мобильное меню -------------------------------------------------- */
  var burger = document.getElementById("burger");
  var nav = document.getElementById("nav");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") nav.classList.remove("is-open");
    });
  }

  /* --- 3. Полоса прочитанного (только на странице статьи) ----------------- */
  var article = document.querySelector(".post__body");
  if (article) {
    var bar = document.createElement("div");
    bar.className = "read-progress";
    bar.innerHTML = "<span></span>";
    document.body.appendChild(bar);
    var fill = bar.firstChild;
    var tick = false;
    var update = function () {
      var r = article.getBoundingClientRect();
      var total = r.height - window.innerHeight;
      var done = total > 0 ? Math.min(1, Math.max(0, -r.top / total)) : 0;
      fill.style.transform = "scaleX(" + done.toFixed(4) + ")";
      tick = false;
    };
    update();
    window.addEventListener("scroll", function () {
      if (!tick) { tick = true; requestAnimationFrame(update); }
    }, { passive: true });
    window.addEventListener("resize", update);
  }

  /* --- 4. Оглавление: подсветка раздела, который читают ------------------- */
  var tocLinks = document.querySelectorAll(".toc a");
  if (tocLinks.length && "IntersectionObserver" in window) {
    var map = {};
    tocLinks.forEach(function (a) {
      var el = document.getElementById(a.getAttribute("href").slice(1));
      if (el) map[el.id] = a;
    });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        tocLinks.forEach(function (a) { a.classList.remove("is-current"); });
        if (map[e.target.id]) map[e.target.id].classList.add("is-current");
      });
    }, { rootMargin: "-12% 0px -70% 0px" });
    Object.keys(map).forEach(function (id) { spy.observe(document.getElementById(id)); });
  }

  /* --- 5. Фильтр по темам в ленте блога ----------------------------------- */
  var filters = document.querySelectorAll(".blog-filter__btn");
  if (filters.length) {
    var cards = document.querySelectorAll(".post-card");
    filters.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var tag = btn.getAttribute("data-filter");
        filters.forEach(function (b) { b.classList.remove("is-active"); });
        btn.classList.add("is-active");
        cards.forEach(function (card) {
          card.hidden = !(tag === "*" || card.getAttribute("data-tag") === tag);
        });
      });
    });
  }
})();
