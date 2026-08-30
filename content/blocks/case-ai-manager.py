# -*- coding: utf-8 -*-
"""Кейс «ИИ-менеджер вместо найма» в виде заполненного шаблона ТЗ.

Идея формата: не рассказ о проекте, а рабочий документ. Читатель видит, как
выглядит хорошо описанная задача, и заодно понимает, что получит сам. Врезки
объясняют, почему формулировка именно такая, — без них это был бы просто дамп.

Всё держится на уровне категорий: клиент под NDA. Цену не публикуем — проект
делался по дружеской ставке и как ориентир вводил бы в заблуждение.
"""
BLOCKS = {
    "ru": [
        ("p", "Ниже — <a href=\"{{HOME}}templates/automation-brief/\">шаблон ТЗ на "
              "автоматизацию</a>, заполненный по реальному проекту. Клиент обезличен, "
              "конкретика сведена к категориям, но структура и логика ответов настоящие."),
        ("p", "Смысл публикации простой. Рассказ о проекте показывает результат. Заполненный "
              "документ показывает <strong>мышление</strong> — и заодно то, что вы получите на "
              "руки, если будете работать со мной. Серые врезки объясняют, почему ответ "
              "сформулирован именно так."),
        ("table", {
            "caption": "Паспорт проекта",
            "head": ["", ""],
            "rows": [
                ["Отрасль", "Логистика и международная торговля"],
                ["Размер", "До 50 человек"],
                ["Год", "2025"],
                ["Срок", "2 месяца"],
                ["Формат", "Внедрение под ключ"],
                ["Результат", "−60% времени на рутину, −40% на разбор почты"],
            ],
        }),

        ("h2", "1. Процесс, а не должность"),
        ("p", "<em>Что делает координатор за неделю:</em>"),
        ("ul", [
            "собирает исходные данные под расчёт сметы из переписки и таблиц;",
            "заполняет смету по шаблону и отправляет на согласование;",
            "готовит комплект документов по сделке из готовых форм;",
            "разбирает входящую почту и раскладывает по типам обращений;",
            "отвечает на типовые запросы статуса;",
            "передаёт нетиповые запросы тем, кто может ответить, и следит за ответом;",
            "сводит данные для бухгалтерии в конце периода;",
            "предлагает вариант логистики из нескольких доступных.",
        ]),
        ("p", "Частота: ежедневно. Оценка трудозатрат: около 30 часов в неделю."),
        ("note", "<strong>Почему так.</strong> Изначально запрос звучал как «нанять ещё одного "
                 "менеджера» — то есть должностью. Пока работа описана должностью, её нельзя "
                 "разделить на то, что автоматизируется, и то, что нет: должность "
                 "автоматизируется либо целиком, либо никак, и оба ответа неверны."),

        ("h2", "2. Где рутина, а где решения"),
        ("table", {
            "caption": "Разметка шагов. Часы — оценка команды, не хронометраж.",
            "head": ["Шаг", "Тип", "Часов в неделю", "Цена ошибки"],
            "rows": [
                ["Сбор данных под смету", "рутина", "6", "Переделка"],
                ["Заполнение сметы по шаблону", "рутина", "4", "Переделка"],
                ["Подготовка комплекта документов", "рутина", "5", "Переделка, иногда задержка сделки"],
                ["Разбор и раскладка почты", "рутина", "6", "Пропущенное письмо"],
                ["Ответы на типовые запросы статуса", "рутина", "3", "Недовольство, не деньги"],
                ["Сведение данных для бухгалтерии", "рутина", "2", "Переделка"],
                ["Какое отклонение поставщика принять", "решение", "1,5", "Прямые потери"],
                ["Когда запросу нужен другой коммерческий ответ", "решение", "1,5", "Потеря клиента"],
                ["Когда эскалировать задержку и кому", "решение", "1", "Потеря клиента"],
            ],
        }),
        ("p", "Итого: <strong>26 часов рутины и 4 часа решений</strong>. Почти вся цена ошибки "
              "живёт в этих четырёх часах."),
        ("note", "<strong>Почему так.</strong> Пропорция 80/20 по времени и обратная по риску — "
                 "самый частый расклад, и именно он ломает наивное «давайте автоматизируем "
                 "роль». Автоматизировав четыре часа решений, вы получите систему, которая "
                 "быстро и уверенно теряет клиентов. Разбор арифметики — в статье "
                 "<a href=\"{{BLOG}}automation-instead-of-hiring/\">автоматизация вместо найма</a>."),

        ("h2", "3. Пригоден ли процесс к автоматизации"),
        ("table", {
            "caption": "Оценка рутинной части, 0–2 по каждой строке",
            "head": ["Критерий", "Балл", "Обоснование"],
            "rows": [
                ["Стабильность на 18 месяцев", "2", "Формы и маршруты не менялись два года"],
                ["Описуемость двумя людьми одинаково", "1", "Расхождения по почте: у каждого своя логика раскладки"],
                ["Доля исключений", "2", "Ниже 5% на сметах и документах"],
                ["Цена ошибки", "2", "Неверная смета ловится на согласовании"],
                ["Проверяемость результата", "2", "Смету смотрит владелец, документы — юрист"],
                ["Необходимость процесса как такового", "1", "Часть сведения для бухгалтерии существует из-за разъехавшихся систем"],
            ],
        }),
        ("p", "<strong>10 из 12.</strong> Порог — 7, так что автоматизировать можно. Две "
              "единицы при этом стали отдельными задачами: договориться о единой логике "
              "раскладки почты до автоматизации и не автоматизировать сведение для "
              "бухгалтерии, а починить источник."),
        ("note", "<strong>Почему так.</strong> Заполнять эту таблицу честно неприятно: она "
                 "почти всегда вскрывает, что часть работы существует только как компенсация "
                 "другой поломки. Автоматизировать компенсацию — значит закрепить поломку "
                 "навсегда."),

        ("h2", "4. Что считается результатом и что считается «готово»"),
        ("h3", "Измеримый результат"),
        ("checklist", [
            "Время координатора на рутину сокращается не менее чем на 40%.",
            "Измеряется оценкой самой команды до и после, по одной и той же анкете.",
            "Замер через два месяца работы нового процесса.",
            "Провалом считается результат ниже 25%: значит, автоматизировали не то.",
        ]),
        ("h3", "Определение готовности"),
        ("checklist", [
            "Процессы собраны, протестированы на реальных данных за прошлый месяц.",
            "Документация написана так, что процесс поднимает другой человек.",
            "Всё живёт в контуре клиента, доступы у клиента.",
            "Назначен владелец — конкретный человек, а не отдел.",
            "Есть ответ на вопрос «как мы узнаем, что это перестало работать правильно».",
        ]),
        ("p", "<em>Недоделанная работа</em> — то, что в определение не вошло, но случится: "
              "договориться о единой логике раскладки почты и починить источник данных для "
              "бухгалтерии. Обе задачи остались за клиентом, обе записаны."),
        ("note", "<strong>Почему так.</strong> Фактический результат вышел −60% и −40% — "
                 "заметно выше порога. Но порог назначался до старта, и это важнее цифры: без "
                 "него любой исход объявляется частичным успехом. И указано, чем измеряем: "
                 "оценка команды — не хронометраж, это порядок величины, а не измерение."),

        ("h2", "5. Границы"),
        ("ul", [
            "<strong>В объёме:</strong> сметы, документы, почта, типовые ответы, уведомления по нетиповым.",
            "<strong>Не в объёме:</strong> бухгалтерский учёт как таковой, ценообразование, переговоры с поставщиками.",
            "<strong>Остаётся ручным сознательно:</strong> все три решения из раздела 2.",
            "<strong>Вторая очередь, если будет:</strong> сведение для бухгалтерии — после того, как починят источник.",
        ]),

        ("h2", "6. Что остаётся у клиента"),
        ("checklist", [
            "Процессы автоматизации в контуре клиента, доступы у клиента.",
            "Шаблоны и таблицы, по которым собираются сметы и документы.",
            "Telegram-бот для разбора почты и внутренней коммуникации.",
            "Документация, достаточная, чтобы поддержать это без автора.",
            "Названный владелец со стороны клиента.",
        ]),
        ("note", "<strong>Почему так.</strong> Этот раздел в шаблонах обычно отсутствует, а в "
                 "спорах всплывает первым. Формулировка «в контуре клиента, доступы у клиента» "
                 "означает, что проект переживает подрядчика: если я исчезну, всё сделанное "
                 "останется работать."),

        ("h2", "7. Стоимость после запуска"),
        ("table", {
            "caption": "Заложено на три года вперёд",
            "head": ["Строка", "Оценка"],
            "rows": [
                ["Поддержка при изменениях у поставщиков данных", "10–15% от стоимости сборки в год"],
                ["Обработка исключений", "Низкая: доля исключений под 5%"],
                ["Проверка, что результат всё ещё верный", "Ежемесячная сверка выборки смет"],
                ["Переделка при изменении процесса", "Не закладывалась: стабильность оценена в 2 балла"],
            ],
        }),

        ("h2", "8. Допуски и эскалация"),
        ("table", {
            "caption": "Согласованы до старта",
            "head": ["Измерение", "Допуск"],
            "rows": [
                ["Время", "+2 недели без согласования"],
                ["Стоимость", "Фиксированная, изменений нет"],
                ["Качество", "Ошибка в смете не чаще 1 на 50"],
                ["Объём", "Обязательны сметы и почта; документы и уведомления желательны"],
                ["Риск", "Остановка при любом сценарии, где данные уходят третьей стороне"],
                ["Выгода", "Ниже 25% экономии — останавливаемся и пересматриваем"],
            ],
        }),
        ("note", "<strong>Почему так.</strong> Строка про риск — единственная, где допуск "
                 "нулевой, и она предопределила главное решение проекта. Смотрите следующий "
                 "раздел."),

        ("h2", "Главное решение проекта, которого нет в шаблоне"),
        ("p", "Запрос был «пусть это делает ИИ». После шести интервью с теми, кто выполняет "
              "работу руками, — менеджерами, бухгалтерами, юристами — от платных языковых "
              "моделей в этом контуре отказались. Шесть причин, в порядке весомости для "
              "клиента:"),
        ("ol", [
            "<strong>Утечка данных.</strong> Коммерческие условия и документы уходили бы третьей стороне.",
            "<strong>Галлюцинации в документах с юридическим весом.</strong> Ошибка в смете ловится, ошибка в формулировке договора — нет.",
            "<strong>Некому отвечать.</strong> За вывод модели не отвечает никто, а без ответственности нет гарантий.",
            "<strong>Склонность к стандартному решению.</strong> Модель уверенно выдаёт типовой ответ там, где случай нетиповой.",
            "<strong>Стоимость</strong> при постоянном потоке обращений.",
            "<strong>Географические ограничения и перебои связи.</strong> Процесс, встающий вместе с чужим сервисом, — это не автоматизация, а новая зависимость.",
        ]),
        ("p", "Поэтому рутина уехала в процессы на n8n с шаблонами и таблицами, а Telegram-бот "
              "взял на себя разбор почты и внутреннюю коммуникацию. Ни одной языковой модели в "
              "контуре."),
        ("q", "Заказчик просил ИИ. Получил результат, который просил, — без ИИ. Это и есть "
              "разница между «сделать как просят» и «решить задачу»."),

        ("h2", "Честная оговорка"),
        ("p", "Цифры — оценка самой команды до и после, за два месяца, а не хронометраж. Это "
              "порядок величины. И проект был спокойным: созвоны раз в неделю, письменные "
              "протоколы, правки там, где нужны. Ничего не ломалось, драмы в кейсе нет — "
              "интересен здесь ответ, а не приключения."),
        ("p", "Отдельная бытовая деталь, которую стоит закладывать в любой удалённый проект по "
              "автоматизации: удалённый рабочий стол приходилось менять по ходу, потому что "
              "разные решения работают в разных сетевых условиях. В итоге прижился RustDesk."),

        ("h2", "Что дальше"),
        ("p", "Если ваша задача выглядит похоже — возьмите "
              "<a href=\"{{HOME}}templates/automation-brief/\">пустой шаблон</a> и заполните "
              "первые три раздела. Этого достаточно, чтобы понять, автоматизировать или "
              "сначала чинить процесс, и чтобы разговаривать с любым подрядчиком предметно."),
        ("p", "Если после заполнения окажется, что задача ваша, а рук нет — "
              "<a href=\"{{SERVICES}}\">форматы работы и цены</a> открыты. Если окажется, что "
              "автоматизировать нечего, шаблон сделал свою работу."),
    ],

    "en": [
        ("p", "Below is the <a href=\"{{HOME}}templates/automation-brief/\">automation brief "
              "template</a>, filled in from a real project. The client is anonymised and the "
              "specifics are reduced to categories, but the structure and the reasoning are real."),
        ("p", "The point of publishing it is simple. A project story shows the result. A filled "
              "document shows the <strong>thinking</strong> — and, incidentally, what you would "
              "receive if you worked with me. The grey notes explain why each answer is worded "
              "the way it is."),
        ("table", {
            "caption": "Project at a glance",
            "head": ["", ""],
            "rows": [
                ["Industry", "Logistics and international trade"],
                ["Size", "Up to 50 people"],
                ["Year", "2025"],
                ["Duration", "2 months"],
                ["Format", "End-to-end implementation"],
                ["Result", "−60% time on routine, −40% on mail triage"],
            ],
        }),

        ("h2", "1. The process, not the job title"),
        ("p", "<em>What the coordinator does in a week:</em>"),
        ("ul", [
            "gathers the inputs for an estimate out of email threads and spreadsheets;",
            "fills the estimate into a template and sends it for approval;",
            "assembles the document set for a deal from existing forms;",
            "triages incoming mail and sorts it by type of request;",
            "answers standard status enquiries;",
            "passes non-standard enquiries to whoever can answer and chases the answer;",
            "consolidates data for the accountants at period end;",
            "proposes one logistics option out of several available.",
        ]),
        ("p", "Frequency: daily. Estimated effort: around 30 hours a week."),
        ("note", "<strong>Why it's written this way.</strong> The original request was \"hire "
                 "another manager\" — that is, phrased as a job title. While work is described "
                 "by a title it cannot be split into what automates and what doesn't: a title "
                 "automates either entirely or not at all, and both answers are wrong."),

        ("h2", "2. Routine versus decisions"),
        ("table", {
            "caption": "Step classification. Hours are the team's estimate, not a stopwatch.",
            "head": ["Step", "Type", "Hours per week", "Cost of an error"],
            "rows": [
                ["Gathering inputs for an estimate", "routine", "6", "Rework"],
                ["Filling the estimate template", "routine", "4", "Rework"],
                ["Assembling the document set", "routine", "5", "Rework, sometimes a delayed deal"],
                ["Triaging and sorting mail", "routine", "6", "A missed email"],
                ["Answering standard status enquiries", "routine", "3", "Annoyance, not money"],
                ["Consolidating data for accounting", "routine", "2", "Rework"],
                ["Which supplier exception to accept", "decision", "1.5", "Direct loss"],
                ["When a request needs a different commercial answer", "decision", "1.5", "A lost client"],
                ["When to escalate a delay, and to whom", "decision", "1", "A lost client"],
            ],
        }),
        ("p", "Totals: <strong>26 hours of routine and 4 hours of decisions</strong>. Almost all "
              "of the cost of error lives in those four hours."),
        ("note", "<strong>Why it's written this way.</strong> An 80/20 split by time and the "
                 "inverse by risk is the most common shape, and it is exactly what breaks the "
                 "naive \"let's automate the role\". Automate the four hours of decisions and "
                 "you get a system that loses clients quickly and confidently. The arithmetic is "
                 "in <a href=\"{{BLOG}}automation-instead-of-hiring/\">automate or hire</a>."),

        ("h2", "3. Is the process fit to automate"),
        ("table", {
            "caption": "Scoring the routine part, 0–2 per line",
            "head": ["Criterion", "Score", "Reasoning"],
            "rows": [
                ["Stability over 18 months", "2", "Forms and routes unchanged for two years"],
                ["Two people describe it identically", "1", "Mail is the exception: everyone sorts by their own logic"],
                ["Exception rate", "2", "Under 5% on estimates and documents"],
                ["Cost of an error", "2", "A wrong estimate is caught at approval"],
                ["Output is verified", "2", "The owner reviews estimates, a lawyer reviews documents"],
                ["The process is needed at all", "1", "Part of the accounting consolidation exists because two systems drifted apart"],
            ],
        }),
        ("p", "<strong>10 out of 12.</strong> The threshold is 7, so automating is justified. The "
              "two scores of 1 became separate tasks: agree a single sorting logic for mail "
              "before automating it, and don't automate the accounting consolidation — fix its "
              "source instead."),
        ("note", "<strong>Why it's written this way.</strong> Filling this table honestly is "
                 "uncomfortable: it almost always reveals that part of the work exists only to "
                 "compensate for another breakage. Automating a compensation means making the "
                 "breakage permanent."),

        ("h2", "4. What counts as the result, and what counts as done"),
        ("h3", "The measurable result"),
        ("checklist", [
            "The coordinator's time on routine falls by at least 40%.",
            "Measured by the team's own before-and-after estimate, using the same questionnaire.",
            "Measured after two months of the new process running.",
            "Below 25% counts as failure: it would mean the wrong thing was automated.",
        ]),
        ("h3", "The definition of done"),
        ("checklist", [
            "Processes built and tested against real data from the previous month.",
            "Documentation written so that somebody else can stand the process up.",
            "Everything lives inside the client's perimeter, with the client holding access.",
            "An owner is named — a person, not a department.",
            "There is an answer to \"how would we know this stopped being correct\".",
        ]),
        ("p", "<em>Undone work</em> — outside the definition but certain to happen: agreeing a "
              "single sorting logic for mail, and fixing the data source behind the accounting "
              "consolidation. Both stayed with the client, both written down."),
        ("note", "<strong>Why it's written this way.</strong> The actual result came out at −60% "
                 "and −40%, well above the threshold. But the threshold was set before the "
                 "start, and that matters more than the number: without it, any outcome gets "
                 "declared a partial success. And the method is stated: a team estimate is not a "
                 "stopwatch — an order of magnitude, not a measurement."),

        ("h2", "5. Boundaries"),
        ("ul", [
            "<strong>In scope:</strong> estimates, documents, mail, standard replies, notifications on non-standard ones.",
            "<strong>Out of scope:</strong> accounting itself, pricing, supplier negotiation.",
            "<strong>Deliberately manual:</strong> all three decisions from section 2.",
            "<strong>Second phase, if any:</strong> the accounting consolidation — once its source is fixed.",
        ]),

        ("h2", "6. What the client keeps"),
        ("checklist", [
            "The automation processes inside the client's perimeter, with the client holding access.",
            "The templates and spreadsheets the estimates and documents are built from.",
            "A Telegram bot for mail triage and internal communication.",
            "Documentation sufficient to maintain it without the author.",
            "A named owner on the client side.",
        ]),
        ("note", "<strong>Why it's written this way.</strong> This section is usually missing "
                 "from templates and is the first to surface in a dispute. \"Inside the client's "
                 "perimeter, client holds access\" means the project outlives the supplier: if I "
                 "disappear, everything built keeps running."),

        ("h2", "7. The cost after launch"),
        ("table", {
            "caption": "Budgeted three years out",
            "head": ["Line", "Estimate"],
            "rows": [
                ["Maintenance when data sources change", "10–15% of build cost per year"],
                ["Exception handling", "Low: exception rate under 5%"],
                ["Checking the output is still correct", "Monthly review of a sample of estimates"],
                ["Rework when the process changes", "Not budgeted: stability scored 2"],
            ],
        }),

        ("h2", "8. Tolerances and escalation"),
        ("table", {
            "caption": "Agreed before the start",
            "head": ["Dimension", "Tolerance"],
            "rows": [
                ["Time", "+2 weeks without approval"],
                ["Cost", "Fixed, no variation"],
                ["Quality", "No more than 1 estimate error in 50"],
                ["Scope", "Estimates and mail mandatory; documents and notifications discretionary"],
                ["Risk", "Stop on any scenario where data leaves for a third party"],
                ["Benefit", "Below 25% saving — stop and reconsider"],
            ],
        }),
        ("note", "<strong>Why it's written this way.</strong> The risk row is the only one with "
                 "zero tolerance, and it determined the project's main decision. See the next "
                 "section."),

        ("h2", "The project's main decision, which isn't in the template"),
        ("p", "The request was \"let AI do this\". After six interviews with the people who do "
              "the work by hand — managers, accountants, lawyers — paid language models were "
              "ruled out for this perimeter. Six reasons, in the order that mattered to the "
              "client:"),
        ("ol", [
            "<strong>Data leakage.</strong> Commercial terms and documents would leave for a third party.",
            "<strong>Hallucinations in documents that carry legal weight.</strong> An error in an estimate gets caught; an error in contract wording does not.",
            "<strong>Nobody to answer for it.</strong> No one is accountable for a model's output, and without accountability there are no guarantees.",
            "<strong>A pull toward the standard answer.</strong> The model confidently produces the typical response where the case is atypical.",
            "<strong>Cost</strong> at a steady volume of requests.",
            "<strong>Geographic restrictions and connectivity gaps.</strong> A process that stalls when somebody else's service does isn't automation, it's a new dependency.",
        ]),
        ("p", "So the routine moved into n8n workflows with templates and spreadsheets, and a "
              "Telegram bot took over mail triage and internal communication. Not one language "
              "model in the perimeter."),
        ("q", "The client asked for AI. They got the result they asked for — without AI. That is "
              "the difference between doing what was requested and solving the problem."),

        ("h2", "The honest caveat"),
        ("p", "The numbers are the team's own before-and-after estimate over two months, not a "
              "stopwatch. Treat them as the order of magnitude. And the project was a calm one: "
              "weekly calls, written minutes, edits where they were needed. Nothing broke; there "
              "is no drama in this case. What's interesting here is the answer, not the adventure."),
        ("p", "One mundane detail worth budgeting into any remote automation project: the remote "
              "desktop tool had to be changed along the way, because different ones work under "
              "different network conditions. RustDesk was what stuck."),

        ("h2", "What next"),
        ("p", "If your problem looks similar, take the "
              "<a href=\"{{HOME}}templates/automation-brief/\">blank template</a> and fill in "
              "the first three sections. That is enough to know whether to automate or fix the "
              "process first, and enough to have a concrete conversation with any supplier."),
        ("p", "If it turns out the problem is yours but the hands aren't — "
              "<a href=\"{{SERVICES}}\">the engagement formats and prices</a> are published. If "
              "it turns out there is nothing worth automating, the template did its job."),
    ],
}
