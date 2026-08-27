/* ==========================================================================
   GANZA CONSULTING — Project Builder ("Собери свой проект")
   Transparent, data-driven effort/duration/budget estimator.
   No frameworks, no build step. Vanilla JS.
   ========================================================================== */
(function () {
  "use strict";

  /* ------------------------------------------------------------------ */
  /* 1. ESTIMATION ENGINE                                                 */
  /* ------------------------------------------------------------------ */
  /*
     Method (openly documented — shown to the user via "How we calculated this"):

     personDays        = scopeUnits × baseDaysPerUnit[type] × readiness × coordination
     personDaysWithRisk = personDays × (1 + riskBuffer)
     teamEfficiency     = clamp(1 − 0.035 × (teamSize − 1), 0.60, 1)   ← coordination overhead as the team grows
     calendarDays       = personDaysWithRisk / (teamSize × teamEfficiency)
     duration range      = calendarDays × [1 − band×0.5 , 1 + band]
     budget (mid)        = personDaysWithRisk × rate[type]              ← cost tracks total effort, not calendar time
     budget range         = budgetMid × [1 − band×0.5 , 1 + band]

     baseDaysPerUnit / rate are calibrated off Ganza's own case studies and
     published pricing tiers — not invented "AI model" coefficients.
  */

  var TYPE_CONFIG = {
    audit: {
      baseDaysPerUnit: 3.5,
      rate: 190,
      label: { ru: "Разбор сложных случаев", en: "Hard-case diagnosis" }
    },
    automation: {
      baseDaysPerUnit: 6,
      rate: 220,
      label: { ru: "Автоматизация нетиповых процессов", en: "Automation for non-standard processes" }
    },
    pm: {
      baseDaysPerUnit: 4.5,
      rate: 180,
      label: { ru: "Управление сложными проектами", en: "Complex project management" }
    },
    web: {
      baseDaysPerUnit: 4,
      rate: 195,
      label: { ru: "Нестандартная веб-разработка", en: "Non-standard web development" }
    }
  };

  var RISK_CONFIG = {
    low: { buffer: 0.10, band: 0.15, label: { ru: "Низкий", en: "Low" } },
    medium: { buffer: 0.20, band: 0.25, label: { ru: "Средний", en: "Medium" } },
    high: { buffer: 0.35, band: 0.40, label: { ru: "Высокий", en: "High" } }
  };

  function clamp(v, min, max) { return Math.max(min, Math.min(max, v)); }

  function calculate(state) {
    var type = TYPE_CONFIG[state.type];
    var risk = RISK_CONFIG[state.risk];
    var scopeUnits = state.scope;
    var readiness = state.readiness;
    var coordination = state.coordination;
    var teamSize = state.team;

    var personDays = scopeUnits * type.baseDaysPerUnit * readiness * coordination;
    var personDaysWithRisk = personDays * (1 + risk.buffer);

    var efficiency = clamp(1 - 0.035 * (teamSize - 1), 0.60, 1);
    var calendarDays = personDaysWithRisk / (teamSize * efficiency);

    var optimisticDays = calendarDays * (1 - risk.band * 0.5);
    var pessimisticDays = calendarDays * (1 + risk.band);

    var budgetMid = personDaysWithRisk * type.rate;
    var budgetLow = budgetMid * (1 - risk.band * 0.5);
    var budgetHigh = budgetMid * (1 + risk.band);

    var weeksLow = Math.max(1, Math.round(optimisticDays / 5));
    var weeksHigh = Math.max(weeksLow + 1, Math.round(pessimisticDays / 5));

    var roundTo = budgetHigh > 3000 ? 100 : 50;

    return {
      weeksLow: weeksLow,
      weeksHigh: weeksHigh,
      daysLow: Math.round(optimisticDays),
      daysHigh: Math.round(pessimisticDays),
      budgetLow: Math.round(budgetLow / roundTo) * roundTo,
      budgetHigh: Math.round(budgetHigh / roundTo) * roundTo,
      efficiency: efficiency,
      risk: risk,
      type: type
    };
  }

  function fmtNum(n) {
    return n.toLocaleString("en-US").replace(/,/g, " ");
  }

  /* ------------------------------------------------------------------ */
  /* 2. QUESTION FLOW                                                     */
  /* ------------------------------------------------------------------ */
  var STEPS = [
    {
      key: "type",
      title: { ru: "ЧТО СОБИРАЕМ?", en: "WHAT ARE WE BUILDING?" },
      sub: { ru: "Выбери, что ближе всего к твоей задаче.", en: "Pick what's closest to your task." },
      breakdownLabel: { ru: "Тип проекта", en: "Project type" },
      options: [
        { value: "audit", label: { ru: "РАЗБОР СЛОЖНЫХ СЛУЧАЕВ", en: "HARD-CASE DIAGNOSIS" } },
        { value: "automation", label: { ru: "АВТОМАТИЗАЦИЯ НЕТИПОВЫХ ПРОЦЕССОВ", en: "AUTOMATION FOR NON-STANDARD PROCESSES" } },
        { value: "pm", label: { ru: "УПРАВЛЕНИЕ СЛОЖНЫМИ ПРОЕКТАМИ", en: "COMPLEX PROJECT MANAGEMENT" } },
        { value: "web", label: { ru: "НЕСТАНДАРТНАЯ ВЕБ-РАЗРАБОТКА", en: "NON-STANDARD WEB DEVELOPMENT" } }
      ]
    },
    {
      key: "scope",
      title: { ru: "КАКОЙ МАСШТАБ?", en: "WHAT SCALE?" },
      sub: { ru: "Сколько процессов, направлений или языковых версий трогаем?", en: "How many processes, areas or language versions are involved?" },
      breakdownLabel: { ru: "Масштаб", en: "Scale" },
      options: [
        { value: 1.5, label: { ru: "ТОЧЕЧНО", en: "PINPOINT" }, hint: { ru: "1–2 направления", en: "1–2 areas" } },
        { value: 4, label: { ru: "НЕСКОЛЬКО", en: "A FEW" }, hint: { ru: "3–5 направлений", en: "3–5 areas" } },
        { value: 8, label: { ru: "МНОГО", en: "A LOT" }, hint: { ru: "6–10 направлений", en: "6–10 areas" } },
        { value: 14, label: { ru: "ВЕСЬ БИЗНЕС", en: "WHOLE BUSINESS" }, hint: { ru: "10+ направлений", en: "10+ areas" } }
      ]
    },
    {
      key: "readiness",
      title: { ru: "НАСКОЛЬКО ВСЁ ОПИСАНО?", en: "HOW DOCUMENTED IS IT?" },
      sub: { ru: "Это влияет на то, сколько времени уйдёт на выяснение «как это вообще работает».", en: "This affects how much time goes into figuring out how things actually work." },
      breakdownLabel: { ru: "Готовность процессов", en: "Process readiness" },
      options: [
        { value: 0.85, label: { ru: "УЖЕ ЗАДОКУМЕНТИРОВАНО", en: "ALREADY DOCUMENTED" } },
        { value: 1.0, label: { ru: "ЧАСТИЧНО, В ГОЛОВАХ У ЛЮДЕЙ", en: "PARTLY, IN PEOPLE'S HEADS" } },
        { value: 1.35, label: { ru: "ПОЛНЫЙ ХАОС", en: "TOTAL CHAOS" }, hint: { ru: "никто не знает, как это работает", en: "nobody knows how it works" } }
      ]
    },
    {
      key: "coordination",
      title: { ru: "СКОЛЬКО ЛЮДЕЙ ЗАДЕЙСТВОВАНО СО СТОРОНЫ КЛИЕНТА?", en: "HOW MANY PEOPLE ARE INVOLVED ON YOUR SIDE?" },
      sub: { ru: "Больше людей — больше согласований и совещаний.", en: "More people means more approvals and meetings." },
      breakdownLabel: { ru: "Координация", en: "Coordination" },
      options: [
        { value: 1.0, label: { ru: "ДО 10", en: "UP TO 10" } },
        { value: 1.15, label: { ru: "10–50", en: "10–50" } },
        { value: 1.3, label: { ru: "50–200", en: "50–200" } },
        { value: 1.5, label: { ru: "200+", en: "200+" } }
      ]
    },
    {
      key: "risk",
      title: { ru: "НАСКОЛЬКО ВСЁ НЕПРЕДСКАЗУЕМО?", en: "HOW UNPREDICTABLE IS THIS?" },
      sub: { ru: "Новые рынки, внешние зависимости и незнакомые технологии — это риск.", en: "New markets, external dependencies and unfamiliar tech all add risk." },
      breakdownLabel: { ru: "Риск / неопределённость", en: "Risk / uncertainty" },
      options: [
        { value: "low", label: { ru: "НИЗКИЙ", en: "LOW" }, hint: { ru: "понятная задача", en: "well-understood task" } },
        { value: "medium", label: { ru: "СРЕДНИЙ", en: "MEDIUM" }, hint: { ru: "есть неизвестные", en: "some unknowns" } },
        { value: "high", label: { ru: "ВЫСОКИЙ", en: "HIGH" }, hint: { ru: "новый рынок / много зависимостей", en: "new market / lots of dependencies" } }
      ]
    },
    {
      key: "team",
      title: { ru: "СКОЛЬКО СПЕЦИАЛИСТОВ МОЖЕТ РАБОТАТЬ ОДНОВРЕМЕННО?", en: "HOW MANY SPECIALISTS CAN WORK IN PARALLEL?" },
      sub: { ru: "Больше людей ускоряет календарный срок, но не снижает общий объём работы.", en: "More people speeds up the calendar, but doesn't shrink the total amount of work." },
      breakdownLabel: { ru: "Команда", en: "Team size" },
      options: [
        { value: 1.5, label: { ru: "1–2 СПЕЦИАЛИСТА", en: "1–2 SPECIALISTS" } },
        { value: 4, label: { ru: "3–5 СПЕЦИАЛИСТОВ", en: "3–5 SPECIALISTS" } },
        { value: 8, label: { ru: "6–10 СПЕЦИАЛИСТОВ", en: "6–10 SPECIALISTS" } }
      ]
    }
  ];

  /* ------------------------------------------------------------------ */
  /* 3. UI CONTROLLER                                                     */
  /* ------------------------------------------------------------------ */
  var state = {};
  var stepIndex = 0;
  var lastResult = null;

  var els = {};

  function lang() {
    return document.documentElement.getAttribute("data-lang") === "en" ? "en" : "ru";
  }

  function t(dict) { return dict[lang()]; }

  function cacheEls() {
    els.overlay = document.getElementById("builderOverlay");
    els.trigger = document.getElementById("builderTrigger");
    els.close = document.getElementById("builderClose");
    els.progressBar = document.getElementById("builderProgressBar");
    els.progressLabel = document.getElementById("builderProgressLabel");
    els.progressWrap = document.getElementById("builderProgress");
    els.stepWrap = document.getElementById("builderStep");
    els.stepTitle = document.getElementById("builderStepTitle");
    els.stepSub = document.getElementById("builderStepSub");
    els.options = document.getElementById("builderOptions");
    els.back = document.getElementById("builderBack");
    els.resultWrap = document.getElementById("builderResult");
    els.duration = document.getElementById("builderDuration");
    els.durationDays = document.getElementById("builderDurationDays");
    els.budget = document.getElementById("builderBudget");
    els.breakdownList = document.getElementById("builderBreakdownList");
    els.breakdown = document.getElementById("builderBreakdown");
    els.telegramCta = document.getElementById("builderTelegramCta");
    els.restart = document.getElementById("builderRestart");
  }

  function openModal(presetType) {
    state = {};
    lastResult = null;
    if (presetType && TYPE_CONFIG[presetType]) {
      state.type = presetType;
      stepIndex = 1; // type already chosen from a service card — start at "scope"
    } else {
      stepIndex = 0;
    }
    els.overlay.classList.add("is-open");
    els.overlay.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    els.resultWrap.hidden = true;
    els.stepWrap.hidden = false;
    els.progressWrap.hidden = false;
    els.progressLabel.hidden = false;
    if (els.breakdown) els.breakdown.open = false;
    renderStep();
  }

  function closeModal() {
    els.overlay.classList.remove("is-open");
    els.overlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  function renderStep() {
    var step = STEPS[stepIndex];

    els.progressBar.style.width = Math.round(((stepIndex + 1) / STEPS.length) * 100) + "%";
    els.progressLabel.textContent =
      (lang() === "ru" ? "ШАГ " : "STEP ") + (stepIndex + 1) + " / " + STEPS.length;

    els.stepTitle.textContent = t(step.title);
    els.stepSub.textContent = t(step.sub);

    els.options.innerHTML = "";
    els.options.classList.toggle("is-single-col", step.options.length <= 2);

    step.options.forEach(function (opt) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "builder-option";
      if (state[step.key] === opt.value) btn.classList.add("is-selected");

      var labelSpan = document.createElement("span");
      labelSpan.textContent = t(opt.label);
      btn.appendChild(labelSpan);

      if (opt.hint) {
        var hintSpan = document.createElement("span");
        hintSpan.className = "builder-option__hint";
        hintSpan.textContent = t(opt.hint);
        btn.appendChild(hintSpan);
      }

      btn.addEventListener("click", function () {
        state[step.key] = opt.value;
        goNext();
      });

      els.options.appendChild(btn);
    });

    els.back.disabled = stepIndex === 0;
  }

  function goNext() {
    if (stepIndex < STEPS.length - 1) {
      stepIndex += 1;
      renderStep();
    } else {
      showResult();
    }
  }

  function goBack() {
    if (stepIndex > 0) {
      stepIndex -= 1;
      renderStep();
    }
  }

  function showResult() {
    lastResult = calculate(state);
    els.stepWrap.hidden = true;
    els.progressWrap.hidden = true;
    els.progressLabel.hidden = true;
    els.resultWrap.hidden = false;
    renderResult();
  }

  function renderResult() {
    if (!lastResult) return;
    var r = lastResult;
    var isRu = lang() === "ru";

    els.duration.textContent = r.weeksLow + "–" + r.weeksHigh + (isRu ? " НЕД." : " WKS");
    els.durationDays.textContent =
      (isRu ? "≈ " : "≈ ") + r.daysLow + "–" + r.daysHigh + (isRu ? " рабочих дней" : " working days");

    els.budget.textContent = "$" + fmtNum(r.budgetLow) + "–" + fmtNum(r.budgetHigh);

    // breakdown
    els.breakdownList.innerHTML = "";
    STEPS.forEach(function (step) {
      var opt = step.options.filter(function (o) { return o.value === state[step.key]; })[0];
      if (!opt) return;
      var li = document.createElement("li");
      li.textContent = t(step.breakdownLabel) + ": " + t(opt.label) + (opt.hint ? " (" + t(opt.hint) + ")" : "");
      els.breakdownList.appendChild(li);
    });
    var effLi = document.createElement("li");
    effLi.textContent = (isRu ? "Эффективность команды при координации: " : "Team efficiency at this coordination load: ") +
      Math.round(r.efficiency * 100) + "%";
    els.breakdownList.appendChild(effLi);
    var riskLi = document.createElement("li");
    riskLi.textContent = (isRu ? "Буфер на риски: +" : "Risk buffer: +") + Math.round(r.risk.buffer * 100) + "%";
    els.breakdownList.appendChild(riskLi);

    // telegram CTA prefilled with a summary
    var summaryLines = [
      isRu ? "Привет! Собрал проект на сайте:" : "Hey! I built a project on the site:",
      (isRu ? "Тип: " : "Type: ") + t(TYPE_CONFIG[state.type].label),
      (isRu ? "Срок: " : "Timeline: ") + r.weeksLow + "–" + r.weeksHigh + (isRu ? " нед." : " wks"),
      (isRu ? "Бюджет: " : "Budget: ") + "$" + fmtNum(r.budgetLow) + "–" + fmtNum(r.budgetHigh),
      isRu ? "Расскажи подробнее?" : "Tell me more?"
    ];
    els.telegramCta.href = "https://t.me/groovebliss?text=" + encodeURIComponent(summaryLines.join("\n"));
  }

  function refreshVisibleLanguage() {
    if (!els.overlay || !els.overlay.classList.contains("is-open")) return;
    if (!els.resultWrap.hidden) {
      renderResult();
    } else {
      renderStep();
    }
  }

  /* ------------------------------------------------------------------ */
  /* 4. WIRE UP                                                           */
  /* ------------------------------------------------------------------ */
  document.addEventListener("DOMContentLoaded", function () {
    cacheEls();
    if (!els.overlay || !els.trigger) return;

    els.trigger.addEventListener("click", openModal);
    els.close.addEventListener("click", closeModal);
    els.back.addEventListener("click", goBack);
    els.restart.addEventListener("click", function () {
      stepIndex = 0;
      state = {};
      lastResult = null;
      els.resultWrap.hidden = true;
      els.stepWrap.hidden = false;
      els.progressWrap.hidden = false;
      els.progressLabel.hidden = false;
      if (els.breakdown) els.breakdown.open = false;
      renderStep();
    });

    els.overlay.addEventListener("click", function (e) {
      if (e.target === els.overlay) closeModal();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeModal();
    });

    var langSwitch = document.getElementById("langSwitch");
    if (langSwitch) {
      langSwitch.addEventListener("click", function () {
        // let script.js flip the attribute first, then re-render visible text
        setTimeout(refreshVisibleLanguage, 0);
      });
    }

    // the header lang switch is hidden behind the modal overlay, so the
    // modal carries its own switch that flips the same html[data-lang]
    var modalLangSwitch = document.getElementById("builderLangSwitch");
    if (modalLangSwitch) {
      modalLangSwitch.addEventListener("click", function () {
        var html = document.documentElement;
        var next = html.getAttribute("data-lang") === "ru" ? "en" : "ru";
        html.setAttribute("data-lang", next);
        html.setAttribute("lang", next);
        refreshVisibleLanguage();
      });
    }

    // service cards double as shortcuts into the builder, preset to that type
    var serviceCells = document.querySelectorAll(".service-cell[data-project-type]");
    serviceCells.forEach(function (cell) {
      cell.addEventListener("click", function () {
        openModal(cell.getAttribute("data-project-type"));
      });
      cell.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " " || e.key === "Spacebar") {
          e.preventDefault();
          openModal(cell.getAttribute("data-project-type"));
        }
      });
    });
  });
})();
