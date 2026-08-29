/* ==========================================================================
   GANZA CONSULTING — форма обратной связи
   --------------------------------------------------------------------------
   Отправляет заявку в Edge Function submit-lead. Клиентская проверка здесь
   только ради вежливых сообщений: настоящая валидация, ограничение частоты
   и ловушка для ботов живут на сервере, потому что консоль браузера открыта
   для всех.
   ========================================================================== */
(function () {
  "use strict";

  var form = document.getElementById("cform");
  if (!form) return;

  var ENDPOINT = form.getAttribute("data-endpoint") || "";
  var status = document.getElementById("cform-status");
  var button = form.querySelector('button[type="submit"]');
  var lang = document.documentElement.getAttribute("lang") || "ru";

  var T = {
    ru: {
      sending: "Отправляю…",
      ok: "Заявка ушла. Отвечу в течение рабочего дня — проверьте почту или телеграм.",
      fields: "Заполните имя, контакт и опишите задачу хотя бы парой предложений.",
      consent: "Без согласия на обработку данных я не смогу вам ответить.",
      rate: "Слишком много отправок подряд. Попробуйте через час или напишите в телеграм.",
      fail: "Не отправилось. Напишите, пожалуйста, в телеграм — так точно дойдёт.",
      offline: "Похоже, нет связи. Проверьте интернет и попробуйте ещё раз."
    },
    en: {
      sending: "Sending…",
      ok: "Sent. I'll reply within one working day — watch your email or Telegram.",
      fields: "Please add your name, a contact, and a couple of sentences about the problem.",
      consent: "I can't reply without your consent to process the data.",
      rate: "Too many submissions in a row. Try in an hour, or message me on Telegram.",
      fail: "That didn't send. Please message me on Telegram — that always gets through.",
      offline: "Looks like you're offline. Check the connection and try again."
    }
  }[lang === "en" ? "en" : "ru"];

  function say(msg, kind) {
    status.textContent = msg;
    status.className = "cform__status" + (kind ? " cform__status--" + kind : "");
  }

  function utm(name) {
    try { return new URLSearchParams(location.search).get(name) || ""; }
    catch (e) { return ""; }
  }
  function session() {
    try { return sessionStorage.getItem("ganza:sid") || ""; } catch (e) { return ""; }
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    var data = {
      name: form.name.value.trim(),
      contact: form.contact.value.trim(),
      message: form.message.value.trim(),
      company: form.company.value.trim(),        // honeypot
      consent: form.consent.checked,
      lang: lang,
      path: location.pathname,
      utm_source: utm("utm_source"),
      utm_medium: utm("utm_medium"),
      utm_campaign: utm("utm_campaign"),
      session_id: session()
    };

    if (!data.consent) { say(T.consent, "err"); form.consent.focus(); return; }
    if (!data.name || data.contact.length < 3 || data.message.length < 10) {
      say(T.fields, "err");
      (!data.name ? form.name : data.contact.length < 3 ? form.contact : form.message).focus();
      return;
    }
    if (!ENDPOINT) { say(T.fail, "err"); return; }

    button.disabled = true;
    say(T.sending);

    fetch(ENDPOINT, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(data)
    })
      .then(function (r) { return r.json().then(function (j) { return { s: r.status, j: j }; }); })
      .then(function (res) {
        if (res.j && res.j.ok) {
          form.reset();
          say(T.ok, "ok");
          document.dispatchEvent(new CustomEvent("ganza:lead"));   // подхватит аналитика
        } else if (res.s === 429) {
          say(T.rate, "err");
        } else if (res.j && res.j.error === "consent") {
          say(T.consent, "err");
        } else if (res.j && res.j.error === "fields") {
          say(T.fields, "err");
        } else {
          say(T.fail, "err");
        }
      })
      .catch(function () { say(navigator.onLine === false ? T.offline : T.fail, "err"); })
      .finally(function () { button.disabled = false; });
  });
})();
