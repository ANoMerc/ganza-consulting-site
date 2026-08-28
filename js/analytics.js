/* ==========================================================================
   GANZA CONSULTING — first-party analytics
   --------------------------------------------------------------------------
   Sends events to a Supabase table. No cookies, no personal data, no
   third-party scripts, nothing that follows anyone to another site.

   >>> SETUP: fill in the two values below with your Supabase project URL and
   >>> the *anon* (public) key. Both are safe to publish: row-level security
   >>> in supabase/schema.sql lets this key insert rows and read nothing.

   What it records
     page_view   every page, with language, referrer, UTM tags, device
     click       every link and button, with its label and section
     outbound    clicks that leave the site (Telegram, LinkedIn, email)
     scroll      25 / 50 / 75 / 100% depth reached  → where people stop
     section     seconds of attention per page section
     engagement  active seconds on the page (only while the tab is visible)
     lang_switch RU/EN toggle use
     builder     progress through the project-builder wizard
   ========================================================================== */
(function () {
  "use strict";

  var CONFIG = {
    url: "https://YOUR-PROJECT.supabase.co",   // <-- Supabase → Settings → API → Project URL
    key: "YOUR-ANON-KEY",                      // <-- Supabase → Settings → API → anon public key
    debug: false                               // true → log events to the console instead of sending
  };

  if (!CONFIG.url || CONFIG.url.indexOf("YOUR-PROJECT") === 0) return; // not configured yet

  // --- storage helpers (fail silently in private mode) ----------------------
  function get(store, k) { try { return window[store].getItem(k); } catch (e) { return null; } }
  function set(store, k, v) { try { window[store].setItem(k, v); } catch (e) { /* ignore */ } }

  function uuid() {
    if (window.crypto && crypto.randomUUID) return crypto.randomUUID();
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
      var r = (Math.random() * 16) | 0;
      return (c === "x" ? r : (r & 0x3) | 0x8).toString(16);
    });
  }

  // --- identity -------------------------------------------------------------
  var SESSION_TTL = 30 * 60 * 1000;
  var visitorId = get("localStorage", "ganza:vid");
  if (!visitorId) { visitorId = uuid(); set("localStorage", "ganza:vid", visitorId); }

  var lastSeen = parseInt(get("localStorage", "ganza:seen") || "0", 10);
  var sessionId = get("sessionStorage", "ganza:sid");
  if (!sessionId || Date.now() - lastSeen > SESSION_TTL) {
    sessionId = uuid();
    set("sessionStorage", "ganza:sid", sessionId);
    set("sessionStorage", "ganza:seq", "0");
  }
  set("localStorage", "ganza:seen", String(Date.now()));

  var seq = parseInt(get("sessionStorage", "ganza:seq") || "0", 10) + 1;
  set("sessionStorage", "ganza:seq", String(seq));

  // --- context --------------------------------------------------------------
  var ua = navigator.userAgent;
  var params = new URLSearchParams(location.search);

  function device() {
    if (/iPad|Tablet|PlayBook|Silk|(Android(?!.*Mobile))/i.test(ua)) return "tablet";
    if (/Mobi|Android|iPhone|iPod|Windows Phone/i.test(ua)) return "mobile";
    return "desktop";
  }
  function browser() {
    if (/Edg\//.test(ua)) return "Edge";
    if (/OPR\/|Opera/.test(ua)) return "Opera";
    if (/YaBrowser/.test(ua)) return "Yandex";
    if (/Firefox\//.test(ua)) return "Firefox";
    if (/Chrome\//.test(ua)) return "Chrome";
    if (/Safari\//.test(ua)) return "Safari";
    return "Other";
  }
  function os() {
    if (/Windows/.test(ua)) return "Windows";
    if (/Android/.test(ua)) return "Android";
    if (/iPhone|iPad|iPod/.test(ua)) return "iOS";
    if (/Mac OS X/.test(ua)) return "macOS";
    if (/Linux/.test(ua)) return "Linux";
    return "Other";
  }
  function pageType() {
    var p = location.pathname;
    if (/\/admin\//.test(p)) return "admin";
    if (/\/blog\/[^/]+\/$/.test(p)) return "article";
    if (/\/blog\/$/.test(p)) return "blog-index";
    if (/\/(ru\/)?$/.test(p) || /index\.html$/.test(p)) return "home";
    return "other";
  }
  function referrerHost() {
    try {
      if (!document.referrer) return null;
      var h = new URL(document.referrer).hostname;
      return h === location.hostname ? null : h;
    } catch (e) { return null; }
  }

  var BASE = {
    visitor_id: visitorId,
    session_id: sessionId,
    path: location.pathname,
    lang: document.documentElement.getAttribute("lang") || "en",
    page_type: pageType(),
    title: document.title.slice(0, 300),
    referrer: (document.referrer || "").slice(0, 500) || null,
    referrer_host: referrerHost(),
    utm_source: params.get("utm_source"),
    utm_medium: params.get("utm_medium"),
    utm_campaign: params.get("utm_campaign"),
    device: device(),
    os: os(),
    browser: browser(),
    viewport_w: window.innerWidth,
    viewport_h: window.innerHeight,
    seq: seq
  };

  // --- transport: batch, and flush with sendBeacon on unload ----------------
  var queue = [];
  var timer = null;
  var ENDPOINT = CONFIG.url.replace(/\/$/, "") + "/rest/v1/events";

  function flush(sync) {
    if (!queue.length) return;
    var body = JSON.stringify(queue);
    queue = [];
    if (CONFIG.debug) { console.log("[ganza-analytics]", JSON.parse(body)); return; }

    if (sync && navigator.sendBeacon) {
      // Supabase accepts the key as a query param, which sendBeacon needs
      var url = ENDPOINT + "?apikey=" + encodeURIComponent(CONFIG.key);
      var blob = new Blob([body], { type: "application/json" });
      if (navigator.sendBeacon(url, blob)) return;
    }
    fetch(ENDPOINT, {
      method: "POST",
      keepalive: true,
      headers: {
        "Content-Type": "application/json",
        "apikey": CONFIG.key,
        "Authorization": "Bearer " + CONFIG.key,
        "Prefer": "return=minimal"
      },
      body: body
    }).catch(function () { /* analytics must never break the page */ });
  }

  function send(event, extra) {
    var row = { event: event };
    for (var k in BASE) row[k] = BASE[k];
    if (extra) for (var j in extra) row[j] = extra[j];
    queue.push(row);
    if (queue.length >= 10) { flush(false); return; }
    clearTimeout(timer);
    timer = setTimeout(function () { flush(false); }, 3000);
  }

  // --- 1. page view ---------------------------------------------------------
  send("page_view");

  // --- 2. clicks ------------------------------------------------------------
  function labelFor(el) {
    var tracked = el.closest("[data-track]");
    if (tracked) return tracked.getAttribute("data-track");
    var text = (el.innerText || el.textContent || "").replace(/\s+/g, " ").trim();
    return (text || el.getAttribute("aria-label") || el.tagName).slice(0, 120);
  }
  function sectionFor(el) {
    var s = el.closest("section[id], header[id], footer[id], article, nav");
    return s ? (s.id || s.tagName.toLowerCase()) : null;
  }

  document.addEventListener("click", function (e) {
    var el = e.target.closest("a, button, summary, [data-track]");
    if (!el) return;

    var href = el.getAttribute("href") || null;
    var external = false;
    if (href) {
      try {
        var u = new URL(href, location.href);
        external = u.hostname !== location.hostname || u.protocol === "mailto:";
        href = u.href.slice(0, 500);
      } catch (err) { external = /^(mailto|tel):/.test(href); }
    }

    send(external ? "outbound" : "click", {
      target: labelFor(el),
      target_href: href,
      section: sectionFor(el)
    });
    if (external) flush(true);
  }, true);

  // --- 3. scroll depth ------------------------------------------------------
  var marks = [25, 50, 75, 100], hit = {};
  function onScroll() {
    var doc = document.documentElement;
    var total = doc.scrollHeight - window.innerHeight;
    var pct = total > 0 ? Math.round((window.scrollY / total) * 100) : 100;
    for (var i = 0; i < marks.length; i++) {
      if (pct >= marks[i] && !hit[marks[i]]) {
        hit[marks[i]] = true;
        send("scroll", { value: marks[i] });
      }
    }
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // --- 4. attention per section --------------------------------------------
  var sectionTime = {}, sectionEnter = {};
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var id = entry.target.id || entry.target.className;
        if (!id) return;
        if (entry.isIntersecting) {
          sectionEnter[id] = Date.now();
        } else if (sectionEnter[id]) {
          sectionTime[id] = (sectionTime[id] || 0) + (Date.now() - sectionEnter[id]) / 1000;
          delete sectionEnter[id];
        }
      });
    }, { threshold: 0.4 });
    document.querySelectorAll("section[id], .post__body, .post__faq, .post__cta, .footer")
      .forEach(function (el) { io.observe(el); });
  }

  // --- 5. active time on page ----------------------------------------------
  var activeMs = 0, activeSince = document.visibilityState === "visible" ? Date.now() : 0;
  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "hidden") {
      if (activeSince) { activeMs += Date.now() - activeSince; activeSince = 0; }
      finish(true);
    } else {
      activeSince = Date.now();
    }
  });

  var finished = false;
  function finish(partial) {
    if (finished) return;
    if (activeSince) { activeMs += Date.now() - activeSince; activeSince = 0; }

    send("engagement", { value: Math.round(activeMs / 1000) });

    Object.keys(sectionEnter).forEach(function (id) {
      sectionTime[id] = (sectionTime[id] || 0) + (Date.now() - sectionEnter[id]) / 1000;
    });
    Object.keys(sectionTime).forEach(function (id) {
      if (sectionTime[id] >= 1) send("section", { section: id.slice(0, 100), value: Math.round(sectionTime[id]) });
    });

    set("localStorage", "ganza:seen", String(Date.now()));
    flush(true);
    if (!partial) finished = true;
    sectionTime = {}; sectionEnter = {}; activeMs = 0;
    if (document.visibilityState === "visible") activeSince = Date.now();
  }
  window.addEventListener("pagehide", function () { finish(false); });

  // --- 6. language switch and project builder ------------------------------
  document.addEventListener("ganza:lang", function (e) {
    send("lang_switch", { target: e.detail && e.detail.lang });
  });

  window.ganzaTrack = function (event, target, value, meta) {
    send(event === "builder" || event === "cta" ? event : "cta", {
      target: target ? String(target).slice(0, 200) : null,
      value: typeof value === "number" ? value : null,
      meta: meta || null
    });
  };
})();
