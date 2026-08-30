# -*- coding: utf-8 -*-
"""Шаблон ТЗ на автоматизацию одного процесса.

Собран из: «Автоматизация вместо найма» (порядок расчёта), «Когда не нужно
автоматизировать» (пригодность процесса, порог исключений, скрытые издержки),
«Консультант по автоматизации» (что должно остаться после), «За что я берусь»
(условия). Формальная рамка — ГОСТ 34.602-2020, от которого этот шаблон
сознательно отличается объёмом.
"""
BLOCKS = {
    "ru": [
        ("p", "Это шаблон для одного процесса, а не для системы. Если вы пишете задание на "
              "внедрение корпоративной системы, берите <strong>ГОСТ 34.602-2020</strong> — "
              "он действующий, и в нём девять разделов, которые требуется сохранить, даже "
              "если требований по ним нет. Для автоматизации одного потока работы это "
              "избыточно: заполнение формы займёт больше времени, чем сама автоматизация."),
        ("p", "Ниже — девять блоков. Заполненные честно, они дают подрядчику всё, что нужно "
              "для оценки, а вам — понимание, стоит ли вообще начинать. Незаполненный блок "
              "тоже информативен: если вы не можете ответить на вопрос, это и есть первый "
              "результат."),
        ("p", "Как он выглядит заполненным по реальному проекту — "
              "<a href=\"{{HOME}}cases/ai-manager/\">разбор кейса «ИИ-менеджер вместо "
              "найма»</a>: те же девять разделов с ответами и пояснениями, почему каждый "
              "сформулирован именно так."),
        ("note", "Правило, которое экономит больше всего: <strong>сначала заполните разделы "
                 "1–3 и остановитесь.</strong> Если после них стало понятно, что процесс надо "
                 "переделать, а не автоматизировать, вы уже сэкономили бюджет внедрения."),

        ("h2", "1. Процесс, а не должность"),
        ("p", "Опишите последовательность шагов так, как она идёт сейчас. Не «менеджер по "
              "логистике», а перечень того, что делается за неделю. Пока работа описана "
              "должностью, её нельзя разделить на то, что автоматизируется, и то, что нет."),
        ("checklist", [
            "Что запускает процесс — письмо, дата, действие клиента, что-то ещё?",
            "Какие шаги идут дальше, по порядку, включая ожидание и согласования.",
            "Кто выполняет каждый шаг и в какой системе.",
            "Чем процесс заканчивается и куда попадает результат.",
            "Сколько раз в неделю или месяц это происходит.",
            "Сколько человеко-часов уходит суммарно — оценка, не хронометраж.",
        ]),
        ("p", "<strong>Проверка:</strong> попросите двух человек описать этот процесс "
              "независимо друг от друга. Если после третьего шага версии расходятся, у вас "
              "не процесс, а привычка с местными вариациями, и автоматизировать её рано."),

        ("h2", "2. Где рутина, а где решения"),
        ("p", "Разметьте каждый шаг из раздела 1 одной из двух меток. <strong>Рутина</strong> — "
              "воспроизводимая последовательность, в которой нет выбора. <strong>Решение</strong> — "
              "точка, где возможны два исхода и один дороже другого."),
        ("table", {
            "caption": "Таблица для заполнения",
            "head": ["Шаг", "Рутина или решение", "Часов в месяц", "Цена ошибки"],
            "rows": [
                ["", "", "", ""],
                ["", "", "", ""],
                ["", "", "", ""],
            ],
        }),
        ("p", "Обычно выясняется, что решений мало по времени и много по риску. Это нормально "
              "и это и есть ответ: автоматизируется рутина, решения остаются человеку — но с "
              "полным контекстом, а не голым уведомлением."),
        ("q", "Шаг, за который кто-то отвечает лично, автоматизируется до состояния «подготовлено "
              "к решению», но не до «решено»."),

        ("h2", "3. Пригоден ли процесс к автоматизации"),
        ("p", "Оцените от 0 до 2 по каждой строке. Меньше 7 из 12 — сначала переделка процесса, "
              "потом разговор о внедрении."),
        ("checklist", [
            "<strong>Стабильность:</strong> процесс будет таким же через 18 месяцев? (0 — изменение уже запланировано)",
            "<strong>Описуемость:</strong> два человека описывают одинаково? (0 — расходятся после третьего шага)",
            "<strong>Доля исключений:</strong> до 5% — 2 балла, 5–20% — 1, выше 20% — 0",
            "<strong>Цена ошибки:</strong> неверный результат дёшево исправить? (0 — стоит клиента или штрафа)",
            "<strong>Проверяемость:</strong> кто-то смотрит на результат и заметит, что он неверный? (0 — не смотрит никто)",
            "<strong>Необходимость:</strong> процесс был бы нужен, если бы починили источник проблемы? (0 — существует только как компенсация)",
        ]),
        ("note", "Доля исключений — самая практичная строка. Выше 20% вы построите три процесса "
                 "вместо одного: автоматизацию, ручной запасной путь и сверку между ними."),

        ("h2", "4. Что считается результатом и что считается «готово»"),
        ("p", "Формулировка вида «стало удобнее» не проверяется и поэтому не годится. Нужны две "
              "разные вещи: измеримый результат и определение готовности."),
        ("h3", "Измеримый результат"),
        ("checklist", [
            "Какая цифра должна измениться и на сколько.",
            "Чем она измеряется сейчас и кто её видит.",
            "Через какой срок замеряем.",
            "Что считается провалом — то есть при каком результате мы признаём, что не вышло.",
        ]),
        ("p", "Последний пункт пропускают чаще всего, и зря: без него любой результат "
              "объявляется частичным успехом."),
        ("h3", "Определение готовности"),
        ("p", "Приём из Large-Scale Scrum, который стоит забрать целиком. Составьте список "
              "условий, при которых работа считается сделанной, — и отдельно список того, что "
              "в него не вошло, но всё равно должно случиться. В LeSS это записывают формулой:"),
        ("q", "Отгружаемое = определение готовности + недоделанная работа."),
        ("p", "Слабое определение готовности опасно не тем, что работа не сделана, а тем, что "
              "она <strong>не запланирована</strong>. Она никуда не исчезает: накапливается "
              "невидимо и всплывает в момент, когда исправлять дороже всего. Классический "
              "пример — отложенное нагрузочное тестирование."),
        ("checklist", [
            "Что должно быть сделано, чтобы считать работу готовой: собрано, протестировано, задокументировано, перенесено в вашу среду, показано команде?",
            "Что в этот список не вошло, но всё равно должно произойти, — и кто это сделает.",
            "Кто подтверждает, что определение готовности выполнено, и по какому признаку.",
        ]),

        ("h2", "5. Границы: что в объёме и что за ним"),
        ("p", "Список того, что <em>не</em> входит, важнее списка того, что входит: именно "
              "оттуда берутся споры на приёмке."),
        ("checklist", [
            "Какие системы затрагиваем и какие не трогаем.",
            "Какие данные передаём подрядчику и в каком виде.",
            "Что остаётся ручным сознательно.",
            "Что делаем во второй очереди, если она будет.",
        ]),

        ("h2", "6. Что остаётся у вас после"),
        ("p", "Раздел, который в шаблонах обычно отсутствует, а в спорах всплывает первым."),
        ("checklist", [
            "Где физически живёт решение — в ваших системах или у подрядчика.",
            "В каком виде отдаются доступы, скрипты, схемы и логика решений.",
            "Есть ли документация, достаточная, чтобы другой человек поддержал это без автора.",
            "Кто именно назван владельцем после запуска — имя, а не отдел.",
            "Как мы узнаем, что автоматизация перестала работать правильно.",
        ]),
        ("q", "Автоматизация без названного владельца становится ничьей за один квартал."),

        ("h2", "7. Стоимость после запуска"),
        ("p", "В смету попадает разработка, а из неё выпадает всё, что начинается на следующий "
              "день. Заложите это заранее, иначе через год окажется, что экономии не было."),
        ("table", {
            "caption": "Что посчитать на три года вперёд, а не на один",
            "head": ["Строка", "Порядок величины", "Ваша оценка"],
            "rows": [
                ["Поддержка при изменениях в смежных системах", "10–20% от стоимости сборки в год", ""],
                ["Обработка исключений", "может превысить саму сборку", ""],
                ["Проверка того, что результат всё ещё верный", "регулярно, а не однократно", ""],
                ["Переделка при изменении процесса", "зависит от стабильности из раздела 3", ""],
            ],
        }),

        ("h2", "8. Допуски и порядок эскалации"),
        ("p", "Приём из PRINCE2, который решает проблему, знакомую всем: о том, что проект "
              "поехал, узнают в момент, когда уже поздно. Лекарство — договориться о допусках "
              "заранее, а не решать каждый раз заново, стоит ли беспокоить заказчика."),
        ("p", "Логика простая. Внутри допуска подрядчик работает сам и не отчитывается сверх "
              "регулярных точек. Как только допуск пробит — сообщает немедленно, и это не "
              "плохая новость, а срабатывание механизма."),
        ("table", {
            "caption": "Шесть измерений допуска. Заполняются до старта.",
            "head": ["Измерение", "Вопрос", "Ваш допуск"],
            "rows": [
                ["Время", "На сколько может сдвинуться срок без согласования?", ""],
                ["Стоимость", "На сколько может вырасти смета без согласования?", ""],
                ["Качество", "В каких пределах результат считается приемлемым?", ""],
                ["Объём", "Что обязательно, а что желательно?", ""],
                ["Риск", "При каком уровне риска нужно остановиться и обсудить?", ""],
                ["Выгода", "При какой ожидаемой отдаче проект перестаёт иметь смысл?", ""],
            ],
        }),
        ("p", "Последняя строка — самая недооценённая. В PRINCE2 есть принцип непрерывного "
              "обоснования: проект должен оставаться оправданным на всём протяжении, а не "
              "только в момент запуска. Если по ходу выяснилось, что экономия будет вдвое "
              "меньше обещанной, честный ответ — остановиться, а не доделать из вежливости."),
        ("note", "Прямо запишите: <strong>кому и в какой форме сообщается о пробитом допуске "
                 "и в какой срок</strong>. Без этого механизм превращается в благое намерение."),

        ("h2", "9. Условия работы"),
        ("checklist", [
            "Кто со стороны заказчика принимает решения и может ответить в течение дня.",
            "К кому подрядчик может обратиться за фактурой — имена людей, которые делают работу руками.",
            "Срок и что происходит при его сдвиге с обеих сторон.",
            "Промежуточные точки: что показывается и как часто.",
            "NDA — подписан до передачи данных или нет.",
        ]),
        ("p", "Первый пункт критичен. Задача без владельца на стороне заказчика не доводится до "
              "результата ни при каком бюджете — подробнее об этом на странице "
              "<a href=\"{{TAKE}}\">за что я берусь и за что нет</a>."),

        ("h2", "Как этим пользоваться"),
        ("steps", [
            ("Заполните разделы 1–3 сами, до разговора с подрядчиками",
             "Занимает пару часов и уже отвечает на главный вопрос: автоматизировать или сначала чинить процесс."),
            ("Отправьте всем подрядчикам один и тот же текст",
             "Разброс оценок по одинаковой постановке говорит о подрядчиках больше, чем их портфолио."),
            ("Смотрите, кто задаёт вопросы по разделам 3 и 6",
             "Тот, кто спрашивает про долю исключений и про владельца после запуска, читал задание. Остальные считали объём."),
            ("Насторожитесь, если никто не сказал «этого делать не надо»",
             "В хорошо заполненном ТЗ почти всегда есть шаг, который стоит отменить, а не автоматизировать."),
            ("Проверьте допуски на исполнимость",
             "Допуск, который невозможно пробить, бесполезен; допуск, который пробивается на первой неделе, означает, что оценка была неправдой."),
        ]),
        ("h2", "Откуда это взято"),
        ("p", "Шаблон намеренно короче формального стандарта, но приёмы в нём не выдуманы. "
              "Разделы 1–3 и 7 собраны из практики и разобраны в статьях "
              "<a href=\"{{BLOG}}automation-instead-of-hiring/\">автоматизация вместо найма</a> и "
              "<a href=\"{{BLOG}}when-not-to-automate/\">когда не нужно автоматизировать</a>. "
              "Определение готовности и понятие недоделанной работы — из Large-Scale Scrum. "
              "Допуски, управление по отклонениям и принцип непрерывного обоснования — из "
              "PRINCE2. Формальная альтернатива для больших систем — ГОСТ 34.602-2020."),
    ],

    "en": [
        ("p", "This is a template for one process, not for a system. If you are writing a "
              "specification for a corporate system rollout, use <strong>GOST 34.602-2020</strong> — "
              "it is current, and it has nine sections that must be retained even when there "
              "are no requirements for them. For automating a single workflow that is "
              "overkill: filling in the form takes longer than the automation."),
        ("p", "Below are nine blocks. Filled in honestly, they give a supplier everything "
              "needed to estimate, and give you an understanding of whether to start at all. "
              "An unfilled block is informative too: if you cannot answer a question, that is "
              "your first result."),
        ("p", "What it looks like filled in from a real project: "
              "<a href=\"{{HOME}}cases/ai-manager/\">the AI manager case</a> — the same nine "
              "sections with answers, annotated with why each is worded the way it is."),
        ("note", "The rule that saves the most: <strong>fill in sections 1–3 and stop.</strong> "
                 "If by then it is clear the process needs redesigning rather than automating, "
                 "you have already saved the implementation budget."),

        ("h2", "1. The process, not the job title"),
        ("p", "Describe the sequence of steps as it runs today. Not \"logistics manager\" but a "
              "list of what actually gets done in a week. While the work is described by a job "
              "title, it cannot be split into what automates and what doesn't."),
        ("checklist", [
            "What starts the process — an email, a date, a customer action, something else?",
            "What steps follow, in order, including waiting and approvals.",
            "Who performs each step, and in which system.",
            "How the process ends and where the output goes.",
            "How many times a week or month this happens.",
            "How many person-hours it takes in total — an estimate, not a stopwatch.",
        ]),
        ("p", "<strong>Test:</strong> ask two people to describe this process independently. If "
              "the versions diverge after step three, you don't have a process — you have a "
              "habit with local variations, and it is too early to automate it."),

        ("h2", "2. Which parts are routine and which are decisions"),
        ("p", "Tag every step from section 1 with one of two labels. <strong>Routine</strong> is "
              "a reproducible sequence containing no choice. A <strong>decision</strong> is a "
              "point where two outcomes are possible and one costs more than the other."),
        ("table", {
            "caption": "Table to fill in",
            "head": ["Step", "Routine or decision", "Hours per month", "Cost of an error"],
            "rows": [["", "", "", ""], ["", "", "", ""], ["", "", "", ""]],
        }),
        ("p", "It usually turns out that decisions are small in time and large in risk. That is "
              "normal, and it is the answer: routine gets automated, decisions stay with a "
              "person — but arriving with full context rather than a bare notification."),
        ("q", "A step somebody answers for personally can be automated up to \"prepared for "
              "decision\" and no further."),

        ("h2", "3. Is the process fit to automate"),
        ("p", "Score each line 0 to 2. Below 7 out of 12 means redesign the process first and "
              "discuss implementation afterwards."),
        ("checklist", [
            "<strong>Stability:</strong> will this be materially the same in 18 months? (0 — a change is already scheduled)",
            "<strong>Definability:</strong> do two people describe it identically? (0 — they diverge after step three)",
            "<strong>Exception rate:</strong> under 5% scores 2, 5–20% scores 1, above 20% scores 0",
            "<strong>Cost of error:</strong> is a wrong output cheap to fix? (0 — it costs a client or a fine)",
            "<strong>Verifiability:</strong> does anyone look at the output and would they notice it was wrong? (0 — nobody looks)",
            "<strong>Necessity:</strong> would this process be needed if the upstream problem were fixed? (0 — it exists only to compensate)",
        ]),
        ("note", "The exception rate is the most practical line. Above 20% you will build three "
                 "processes instead of one: the automation, the manual fallback, and a "
                 "reconciliation between them."),

        ("h2", "4. What counts as the result, and what counts as \"done\""),
        ("p", "A formulation like \"it will be more convenient\" cannot be checked and therefore "
              "won't do. You need two separate things: a measurable result and a definition of done."),
        ("h3", "The measurable result"),
        ("checklist", [
            "Which number should change, and by how much.",
            "How it is measured today and who sees it.",
            "When we measure.",
            "What counts as failure — at which result do we agree it didn't work.",
        ]),
        ("p", "The last point is the one most often skipped, and skipping it means any outcome "
              "gets declared a partial success."),
        ("h3", "The definition of done"),
        ("p", "A practice worth taking wholesale from Large-Scale Scrum. Write the list of "
              "conditions under which the work counts as finished — and separately, the list of "
              "what didn't make it into that definition but still has to happen. LeSS writes it "
              "as a formula:"),
        ("q", "Potentially shippable = definition of done + undone work."),
        ("p", "A weak definition of done is dangerous not because work is left unfinished but "
              "because that work is <strong>unplanned</strong>. It doesn't disappear: it "
              "accumulates invisibly and surfaces when fixing it costs the most. The classic "
              "example is deferred performance testing."),
        ("checklist", [
            "What has to be true to call the work done: built, tested, documented, moved into your environment, demonstrated to the team?",
            "What isn't on that list but still has to happen — and who will do it.",
            "Who confirms the definition of done was met, and on what evidence.",
        ]),

        ("h2", "5. Boundaries: in scope and out of it"),
        ("p", "The list of what is <em>not</em> included matters more than the list of what is: "
              "that is where acceptance disputes come from."),
        ("checklist", [
            "Which systems we touch and which we leave alone.",
            "What data goes to the supplier, and in what form.",
            "What stays manual deliberately.",
            "What belongs to a second phase, if there is one.",
        ]),

        ("h2", "6. What you keep afterwards"),
        ("p", "The section usually missing from templates, and the first one to surface in a dispute."),
        ("checklist", [
            "Where the solution physically lives — in your systems or the supplier's.",
            "In what form access, scripts, schemas and decision logic are handed over.",
            "Whether documentation is sufficient for someone else to maintain it without the author.",
            "Who exactly is named owner after launch — a person, not a department.",
            "How we will know the automation has stopped being correct.",
        ]),
        ("q", "Automation with nobody named as its owner becomes nobody's within a quarter."),

        ("h2", "7. The cost after launch"),
        ("p", "The estimate covers the build and omits everything that starts the next day. "
              "Budget it up front, or a year from now it will turn out there was no saving."),
        ("table", {
            "caption": "Cost these three years out, not one",
            "head": ["Line", "Order of magnitude", "Your estimate"],
            "rows": [
                ["Maintenance when neighbouring systems change", "10–20% of build cost per year", ""],
                ["Exception handling", "can exceed the build itself", ""],
                ["Checking that the output is still correct", "recurring, not one-off", ""],
                ["Rework when the process changes", "depends on stability from section 3", ""],
            ],
        }),

        ("h2", "8. Tolerances and escalation"),
        ("p", "A practice from PRINCE2 that solves a problem everyone recognises: you find out "
              "the project has drifted at the point where it is already too late. The remedy is "
              "to agree tolerances up front rather than deciding each time whether the news is "
              "worth troubling the client with."),
        ("p", "The logic is simple. Inside the tolerance the supplier works unsupervised and "
              "reports only at the regular checkpoints. The moment a tolerance is breached they "
              "say so immediately — and that is not bad news, it is the mechanism working."),
        ("table", {
            "caption": "Six tolerance dimensions. Agreed before the start.",
            "head": ["Dimension", "Question", "Your tolerance"],
            "rows": [
                ["Time", "How far can the date move without approval?", ""],
                ["Cost", "How far can the estimate rise without approval?", ""],
                ["Quality", "Within what bounds is the output acceptable?", ""],
                ["Scope", "What is mandatory and what is discretionary?", ""],
                ["Risk", "At what level of risk do we stop and discuss?", ""],
                ["Benefit", "At what expected return does the project stop making sense?", ""],
            ],
        }),
        ("p", "The last row is the most underrated. PRINCE2 has a principle of continued "
              "business justification: a project must stay justified throughout, not only at "
              "launch. If it emerges along the way that the saving will be half what was "
              "promised, the honest answer is to stop, not to finish out of politeness."),
        ("note", "Write down explicitly: <strong>who is told about a breached tolerance, in what "
                 "form, and within what time</strong>. Without that the mechanism becomes a good intention."),

        ("h2", "9. Working conditions"),
        ("checklist", [
            "Who on your side makes decisions and can answer within a day.",
            "Who the supplier may approach for detail — the names of people who do the work by hand.",
            "The deadline, and what happens if either side moves it.",
            "Checkpoints: what gets shown, and how often.",
            "NDA — signed before data is handed over, or not.",
        ]),
        ("p", "The first point is critical. A problem with no owner on the client side does not "
              "reach a result at any budget — more on that on the page "
              "<a href=\"{{TAKE}}\">what I take on and what I decline</a>."),

        ("h2", "How to use this"),
        ("steps", [
            ("Fill in sections 1–3 yourself, before talking to any supplier",
             "It takes a couple of hours and already answers the main question: automate, or fix the process first."),
            ("Send every supplier exactly the same text",
             "The spread of estimates against an identical brief tells you more about suppliers than their portfolios do."),
            ("Watch who asks questions about sections 3 and 6",
             "Whoever asks about the exception rate and about the owner after launch has read the brief. The others counted scope."),
            ("Be wary if nobody says \"you shouldn't do this part\"",
             "A well-filled brief almost always contains a step that should be cancelled rather than automated."),
            ("Sanity-check the tolerances",
             "A tolerance that cannot be breached is useless; one breached in the first week means the estimate wasn't true."),
        ]),
        ("h2", "Where this comes from"),
        ("p", "The template is deliberately shorter than the formal standard, but the practices "
              "in it are not invented. Sections 1–3 and 7 come from practice and are worked "
              "through in <a href=\"{{BLOG}}automation-instead-of-hiring/\">automate or hire</a> and "
              "<a href=\"{{BLOG}}when-not-to-automate/\">when not to automate</a>. The definition "
              "of done and the notion of undone work come from Large-Scale Scrum. Tolerances, "
              "management by exception and continued business justification come from PRINCE2. "
              "The formal alternative for large systems is GOST 34.602-2020."),
    ],
}
