(function () {
  "use strict";

  var html = document.documentElement;
  var langSwitch = document.getElementById("langSwitch");
  var burger = document.getElementById("burger");
  var nav = document.getElementById("nav");

  // ---- language toggle (in-memory only, defaults to RU) ----
  function setLang(lang) {
    html.setAttribute("data-lang", lang);
    html.setAttribute("lang", lang);
  }

  if (langSwitch) {
    langSwitch.addEventListener("click", function () {
      var current = html.getAttribute("data-lang") === "ru" ? "en" : "ru";
      setLang(current);
    });
  }

  // ---- mobile nav ----
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
})();
