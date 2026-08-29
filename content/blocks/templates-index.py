# -*- coding: utf-8 -*-
"""Хаб шаблонов и чек-листов."""
BLOCKS = {
    "ru": [
        ("p", "Заготовки, которыми я пользуюсь сам. Ничего не нужно оставлять взамен: "
              "страницы открыты, печатаются и сохраняются в PDF из браузера."),
        ("p", "Каждая собрана из практики и из статей этого блога, а приёмы, которые я взял "
              "у других, названы своими именами: определение готовности и недоделанная работа — "
              "из Large-Scale Scrum, допуски и управление по отклонениям — из PRINCE2, "
              "формальная альтернатива для больших систем — ГОСТ 34.602-2020."),

        ("h2", "Шаблон ТЗ на автоматизацию одного процесса"),
        ("p", "Девять разделов вместо девяти обязательных разделов стандарта. Заполните первые "
              "три — и уже станет понятно, автоматизировать или сначала чинить процесс. "
              "<a href=\"{{HOME}}templates/automation-brief/\">Открыть шаблон →</a>"),

        ("h2", "Чек-лист: нанимать или автоматизировать"),
        ("p", "Две таблицы полной стоимости — сотрудника и автоматизации, — разделение работы на "
              "рутину и решения и проверка на ответственность. Час работы до разговора с "
              "подрядчиком. <a href=\"{{HOME}}templates/automate-or-hire/\">Открыть чек-лист →</a>"),

        ("h2", "Чек-лист выбора подрядчика"),
        ("p", "Пять вопросов с разбором того, как звучит хороший и плохой ответ, четыре гарантии "
              "непрерывности, которые стоит требовать, и признаки раздутого объёма. "
              "<a href=\"{{HOME}}templates/choosing-a-supplier/\">Открыть чек-лист →</a>"),

        ("h2", "Шаблон протокола решения"),
        ("p", "Кто что сказал, кому что поручено, что решено — и, отдельно, что считается "
              "сделанным, а что в это определение не вошло, но всё равно должно случиться. "
              "Для команд, которые работают асинхронно. "
              "<a href=\"{{HOME}}templates/decision-record/\">Открыть шаблон →</a>"),

        ("note", "Если после заполнения окажется, что задача ваша, а рук нет — "
                 "<a href=\"{{SERVICES}}\">посмотрите форматы работы</a>. Если окажется, что "
                 "автоматизировать нечего, значит шаблон сделал свою работу."),
    ],
    "en": [
        ("p", "The working documents I use myself. Nothing to hand over in exchange: the pages "
              "are open, they print, and the browser will save them as PDF."),
        ("p", "Each is assembled from practice and from this blog, and the practices I borrowed "
              "are named: the definition of done and undone work come from Large-Scale Scrum, "
              "tolerances and management by exception from PRINCE2, and the formal alternative "
              "for large systems is GOST 34.602-2020."),

        ("h2", "Automation brief for one process"),
        ("p", "Nine sections instead of the standard's nine mandatory ones. Fill in the first "
              "three and it is already clear whether to automate or fix the process first. "
              "<a href=\"{{HOME}}templates/automation-brief/\">Open the template →</a>"),

        ("h2", "Checklist: automate or hire"),
        ("p", "Two full-cost tables — the employee and the automation — the split between routine "
              "and decisions, and a test for accountability. An hour's work before you talk to a "
              "supplier. <a href=\"{{HOME}}templates/automate-or-hire/\">Open the checklist →</a>"),

        ("h2", "Checklist: choosing a supplier"),
        ("p", "Five questions with what a good and a bad answer sounds like, four continuity "
              "guarantees worth demanding, and the signs of inflated scope. "
              "<a href=\"{{HOME}}templates/choosing-a-supplier/\">Open the checklist →</a>"),

        ("h2", "Decision record"),
        ("p", "Who said what, who got which task, what was decided — and separately what counts "
              "as done and what didn't make that definition but still has to happen. For teams "
              "working asynchronously. "
              "<a href=\"{{HOME}}templates/decision-record/\">Open the template →</a>"),

        ("note", "If filling one in shows the problem is yours but the hands aren't — "
                 "<a href=\"{{SERVICES}}\">look at the engagement formats</a>. If it shows there "
                 "is nothing worth automating, the template did its job."),
    ],
}
