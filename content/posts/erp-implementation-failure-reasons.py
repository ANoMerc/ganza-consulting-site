# -*- coding: utf-8 -*-
POST = dict(
    slug="erp-implementation-failure-reasons",
    date="2026-07-28",
    updated="2026-08-27",
    tag={"en": "Project Management", "ru": "Управление проектами"},
    title={
        "en": "Why ERP Implementations Fail: 7 Failure Modes and the Early Signal for Each",
        "ru": "Почему проваливаются внедрения ERP: 7 сценариев отказа и ранний сигнал каждого",
    },
    h1={
        "en": "Why ERP Implementations Fail: 7 Failure Modes and the Early Signal for Each",
        "ru": "Почему проваливаются внедрения ERP: 7 сценариев отказа и ранний сигнал каждого",
    },
    dek={
        "en": "The publicly documented disasters share a small number of mechanisms. Each one emits a specific signal months before the write-off — if anyone is watching for it.",
        "ru": "У публично задокументированных катастроф общий небольшой набор механизмов. Каждый подаёт конкретный сигнал за месяцы до списания — если кто-то за ним следит.",
    },
    description={
        "en": "Seven recurring ERP failure modes drawn from publicly documented cases, the early warning signal each produces, cheap countermeasures, and a pre-go-live checklist that catches most of them.",
        "ru": "Семь повторяющихся сценариев провала ERP на основе публично задокументированных кейсов, ранний сигнал каждого, дешёвые контрмеры и чек-лист перед запуском, ловящий большинство из них.",
    },
    keywords={
        "en": "ERP implementation failure, why ERP projects fail, SAP implementation risks, ERP go-live checklist, data migration failure, change management ERP, ERP project governance, system implementation risk",
        "ru": "провал внедрения ERP, почему проваливаются ERP-проекты, риски внедрения SAP, чек-лист перед запуском ERP, провал миграции данных, управление изменениями при внедрении, управление ERP-проектом, риски внедрения систем",
    },
    hashtags=["ERP", "ProjectManagement", "DigitalTransformation", "ChangeManagement", "RiskManagement"],
    related=["lidl-digital-transformation-failure", "when-not-to-automate", "audit-nobody-reads"],
    body={
        "en": [
            ("p", "ERP failures are unusually well documented, because they are large enough to appear in earnings statements and lawsuits. That makes them useful: the public record shows the same small set of mechanisms repeating across decades, vendors and industries."),
            ("p", "This is not a list of causes like \"poor planning\" — that describes everything and predicts nothing. Below are seven <strong>specific failure modes</strong>, each with the early signal it emits, the reason that signal gets ignored, and a countermeasure that costs almost nothing."),

            ("h2", "What the public record actually shows"),
            ("table", {
                "caption": "Publicly reported ERP failures and their reported cost (figures vary between sources)",
                "head": ["Company", "Period", "Reported impact", "Dominant mechanism"],
                "rows": [
                    ["Hershey's", "1999", "≈$100m in unshipped orders during peak season", "Compressed timeline; go-live scheduled into the busiest quarter"],
                    ["Nike", "2000–2001", "≈$100m in lost sales attributed to demand planning", "Forecasting logic trusted before it was validated against reality"],
                    ["Waste Management", "2005–2010", "$500m lawsuit, settled out of court", "Gap between demonstrated capability and delivered product"],
                    ["National Grid", "2012–2014", "≈$585m in recovery costs", "Go-live with unresolved data and testing gaps"],
                    ["LeasePlan", "2016–2019", "≈$119m written off", "Scope and complexity outrunning the delivery model"],
                    ["Revlon", "2018", "Reported $64m in lost sales; shareholder litigation", "Fulfilment disruption after go-live"],
                    ["Haribo", "2018", "Reported delivery failures and a sharp sales drop", "Supply chain data and process readiness"],
                    ["Lidl", "2011–2018", "≈€500m before cancellation", "Customising core logic instead of changing the process"],
                ],
            }),
            ("p", "Notice how few of these are software defects. Almost every case is a decision about process, data, timing or governance that the software then faithfully executed. The <a href=\"../lidl-digital-transformation-failure/\">Lidl case is worth reading in full</a> because it demonstrates the slowest and most expensive version of the pattern."),

            ("h2", "Failure mode 1: customising the product instead of changing the process"),
            ("p", "The organisation has a process it considers a competitive advantage. The standard product does it differently. Rather than change the process, the software is changed."),
            ("ul", [
                "<strong>Early signal:</strong> the list of deviations from standard grows past a handful and starts touching core data models — valuation, master data, document flow.",
                "<strong>Why it's ignored:</strong> each deviation is individually justified and individually small.",
                "<strong>Countermeasure:</strong> maintain a single visible register of permanent deviations with a named owner for each, and estimate the cost of applying the vendor's next two major releases on top of them. That estimate is the real price of the customisation, and it's usually nobody's job to produce it.",
            ]),

            ("h2", "Failure mode 2: a go-live date fixed before the scope"),
            ("p", "A date is announced — to a board, a market, or an expiring licence — and scope is then negotiated backwards against it. Testing is the compressible item, so testing compresses."),
            ("ul", [
                "<strong>Early signal:</strong> scope is being cut in test phases rather than in build phases, and cutover rehearsals keep moving.",
                "<strong>Why it's ignored:</strong> the date has a public commitment attached; the testing reduction does not.",
                "<strong>Countermeasure:</strong> declare in advance which quarter is off-limits for go-live. Hershey's is the canonical example — going live into the peak season converts a technical problem into unshipped revenue.",
            ]),

            ("h2", "Failure mode 3: data migration treated as an IT task"),
            ("p", "Migration is scoped as moving records between systems. It is actually a business exercise in deciding what the records mean — which duplicates are the same customer, which historic prices are still valid, which product codes are dead."),
            ("ul", [
                "<strong>Early signal:</strong> nobody outside IT has signed off on data quality criteria, and the first full-volume migration rehearsal is scheduled late.",
                "<strong>Why it's ignored:</strong> it looks technical, so it's delegated technically.",
                "<strong>Countermeasure:</strong> a named business owner per data domain who signs off on quality thresholds, and at least two full-volume rehearsals with reconciliation against the source, the first one early enough that its findings can change the plan.",
            ]),

            ("h2", "Failure mode 4: change management funded as training"),
            ("p", "The budget contains training days. It does not contain time for people to be slower for eight weeks, or capacity for the workarounds they will invent, or a route for the front line to report that the new process doesn't fit reality."),
            ("ul", [
                "<strong>Early signal:</strong> the plan assumes productivity returns to baseline within days of go-live; no post-go-live capacity buffer exists.",
                "<strong>Why it's ignored:</strong> a productivity dip is uncomfortable to put in a business case.",
                "<strong>Countermeasure:</strong> budget an explicit productivity dip — commonly 20–40% for four to eight weeks in affected functions — and staff a hypercare team with authority to change configuration, not just to log tickets.",
            ]),

            ("h2", "Failure mode 5: governance that measures activity, not viability"),
            ("p", "Steering committees receive milestone completion, tickets closed, modules configured. All of these can be green while the answer to \"can this run our largest market at real volume?\" is getting worse."),
            ("ul", [
                "<strong>Early signal:</strong> status reporting is consistently amber-to-green while informal conversation with practitioners is consistently pessimistic.",
                "<strong>Why it's ignored:</strong> the gap only shows up if someone deliberately compares the two, and nobody owns that comparison.",
                "<strong>Countermeasure:</strong> one quarterly, consequence-free conversation with practitioners, conducted off the reporting line by someone senior enough to act. It is the cheapest early-warning system available and it is almost never run.",
            ]),
            ("q", "By the time a status report turns red, the information that should have turned it red has usually been available for two quarters."),

            ("h2", "Failure mode 6: testing the happy path at convenient volume"),
            ("p", "Testing validates that the system does what the design says, using clean data, at comfortable volume, in the pilot market. Production is none of those things."),
            ("ul", [
                "<strong>Early signal:</strong> no performance test has been run at peak historical volume; exception scenarios are documented but not executed.",
                "<strong>Why it's ignored:</strong> peak-volume testing requires production-like data and infrastructure, which is expensive and easy to defer.",
                "<strong>Countermeasure:</strong> pick the highest-intensity market or period in your history and prove the system there before committing. Pilots in small markets prove change management, not capacity — this is precisely where Lidl's customised design ran out of road.",
            ]),

            ("h2", "Failure mode 7: retiring the fallback too early"),
            ("p", "The legacy system is switched off, or allowed to fall out of sync, before the new one has run a full business cycle at full volume. What was a project failure becomes an operational crisis with no route back."),
            ("ul", [
                "<strong>Early signal:</strong> there is no written, tested rollback procedure, or the legacy system has stopped receiving data.",
                "<strong>Why it's ignored:</strong> maintaining two systems is expensive and feels like a lack of confidence.",
                "<strong>Countermeasure:</strong> keep the fallback viable through at least one complete business cycle — a month-end, a quarter-end, a peak season — and test the rollback once for real. Lidl's ability to return to its legacy system is the main reason a €500m write-off wasn't worse.",
            ]),

            ("h2", "Pre-go-live checklist"),
            ("p", "None of these require new tooling. All of them can be answered yes or no in a single steering meeting."),
            ("checklist", [
                "A single register of permanent deviations from standard exists, with a named owner per item.",
                "The cost of applying the vendor's next two major releases has been estimated and accepted.",
                "Go-live is not scheduled into a peak trading period, and the excluded quarters were declared in advance.",
                "Each data domain has a business owner who has signed off on quality thresholds.",
                "At least two full-volume migration rehearsals have completed, with reconciliation against source.",
                "A performance test has run at peak historical volume, not at convenient volume.",
                "Exception scenarios have been executed, not just documented.",
                "A productivity dip is budgeted, with a hypercare team empowered to change configuration.",
                "A written rollback procedure exists and has been tested once.",
                "The legacy system will remain viable through at least one full business cycle.",
                "Written kill criteria exist for the next milestone, agreed before the date.",
                "A consequence-free practitioner conversation has happened this quarter, off the reporting line.",
            ]),

            ("h2", "If you're already inside one"),
            ("steps", [
                ("Separate viability from activity in this week's reporting",
                 "Ask one question the status report does not answer: what evidence exists that this will run our largest market at real volume? If the answer is a plan rather than a test result, that is your position."),
                ("Get the deviation register onto one page",
                 "If it doesn't exist, building it is a two-day job and it is usually the most informative document anyone produces on the programme."),
                ("Write kill criteria for the next milestone, now",
                 "Specific, measurable, agreed before the date arrives. Criteria written after a slip are negotiations."),
                ("Protect the fallback",
                 "Whatever else is decided, keep the old system able to run. This converts the worst case from a crisis into an expensive disappointment."),
                ("Decide who is allowed to say stop",
                 "Programmes become cancellable only when the people identified with them are no longer the only ones who can end them. Name that person explicitly, in advance."),
            ]),
            ("note", "The uncomfortable pattern in the public record: almost every one of these programmes could have been stopped for a fraction of its final cost, and almost none of them were, because at every individual decision point continuing was cheaper than stopping."),
        ],
        "ru": [
            ("p", "Провалы ERP необычно хорошо задокументированы, потому что они достаточно велики, чтобы попадать в отчётность и судебные иски. Это делает их полезными: публичные записи показывают, как один и тот же небольшой набор механизмов повторяется десятилетиями, у разных вендоров и в разных отраслях."),
            ("p", "Это не список причин вроде «плохое планирование» — такая формулировка описывает всё и не предсказывает ничего. Ниже семь <strong>конкретных сценариев отказа</strong>, у каждого — ранний сигнал, причина, по которой сигнал игнорируют, и контрмера, стоящая почти ноль."),

            ("h2", "Что показывает публичная запись"),
            ("table", {
                "caption": "Публично известные провалы ERP и заявленный ущерб (цифры у разных источников различаются)",
                "head": ["Компания", "Период", "Заявленное влияние", "Основной механизм"],
                "rows": [
                    ["Hershey's", "1999", "≈$100 млн неотгруженных заказов в пик сезона", "Сжатые сроки; запуск назначен на самый нагруженный квартал"],
                    ["Nike", "2000–2001", "≈$100 млн потерянных продаж из-за планирования спроса", "Логике прогнозирования доверились до проверки на реальности"],
                    ["Waste Management", "2005–2010", "Иск на $500 млн, урегулирован во внесудебном порядке", "Разрыв между продемонстрированными возможностями и поставленным продуктом"],
                    ["National Grid", "2012–2014", "≈$585 млн затрат на восстановление", "Запуск с нерешёнными вопросами по данным и тестированию"],
                    ["LeasePlan", "2016–2019", "≈$119 млн списано", "Объём и сложность обогнали модель поставки"],
                    ["Revlon", "2018", "Заявлено $64 млн потерянных продаж; иски акционеров", "Сбой отгрузок после запуска"],
                    ["Haribo", "2018", "Сообщалось о срывах поставок и резком падении продаж", "Готовность данных и процессов цепочки поставок"],
                    ["Lidl", "2011–2018", "≈€500 млн до отмены", "Доработка базовой логики вместо изменения процесса"],
                ],
            }),
            ("p", "Обратите внимание, как мало здесь дефектов ПО. Почти в каждом случае это решение о процессе, данных, сроках или управлении, которое система затем добросовестно исполнила. <a href=\"../lidl-digital-transformation-failure/\">Кейс Lidl стоит прочитать целиком</a> — он демонстрирует самую медленную и дорогую версию этого паттерна."),

            ("h2", "Сценарий 1: доработка продукта вместо изменения процесса"),
            ("p", "У организации есть процесс, который она считает конкурентным преимуществом. Стандартный продукт делает это иначе. Вместо изменения процесса меняют систему."),
            ("ul", [
                "<strong>Ранний сигнал:</strong> список отклонений от стандарта перерастает несколько пунктов и начинает затрагивать базовые модели данных — оценку, мастер-данные, документооборот.",
                "<strong>Почему игнорируется:</strong> каждое отклонение по отдельности обосновано и по отдельности невелико.",
                "<strong>Контрмера:</strong> ведите единый видимый реестр постоянных отклонений с названным владельцем каждого и оцените стоимость накатывания двух следующих мажорных релизов вендора поверх них. Эта оценка и есть настоящая цена доработки, и обычно её никто не обязан считать.",
            ]),

            ("h2", "Сценарий 2: дата запуска зафиксирована раньше объёма"),
            ("p", "Дата объявлена — совету директоров, рынку или под истекающую лицензию, — и объём затем подгоняется под неё в обратную сторону. Сжимаемый элемент — тестирование, поэтому тестирование и сжимается."),
            ("ul", [
                "<strong>Ранний сигнал:</strong> объём режут на фазах тестирования, а не на фазах разработки, а репетиции переноса продолжают сдвигаться.",
                "<strong>Почему игнорируется:</strong> у даты есть публичное обязательство, у сокращения тестов — нет.",
                "<strong>Контрмера:</strong> заранее объявите, в какой квартал запуск невозможен. Hershey's — канонический пример: запуск в пик сезона превращает техническую проблему в неотгруженную выручку.",
            ]),

            ("h2", "Сценарий 3: миграция данных как ИТ-задача"),
            ("p", "Миграцию описывают как перенос записей между системами. На деле это бизнес-упражнение по определению того, что записи означают: какие дубли — один и тот же клиент, какие исторические цены ещё действуют, какие коды товаров мертвы."),
            ("ul", [
                "<strong>Ранний сигнал:</strong> никто вне ИТ не подписал критерии качества данных, а первая полнообъёмная репетиция миграции назначена поздно.",
                "<strong>Почему игнорируется:</strong> задача выглядит технической, поэтому и делегируется технически.",
                "<strong>Контрмера:</strong> названный бизнес-владелец по каждому домену данных, подписывающий пороги качества, и минимум две полнообъёмные репетиции со сверкой с источником, причём первая — достаточно рано, чтобы её результаты могли изменить план.",
            ]),

            ("h2", "Сценарий 4: управление изменениями профинансировано как обучение"),
            ("p", "В бюджете есть дни обучения. В нём нет времени на то, что люди будут медленнее восемь недель, нет ёмкости под обходные пути, которые они изобретут, и нет канала, по которому передовая линия сообщит, что новый процесс не совпадает с реальностью."),
            ("ul", [
                "<strong>Ранний сигнал:</strong> план исходит из того, что производительность вернётся к норме через несколько дней после запуска; буфера ёмкости после запуска нет.",
                "<strong>Почему игнорируется:</strong> провал производительности неудобно вписывать в обоснование проекта.",
                "<strong>Контрмера:</strong> заложите явное падение производительности — обычно 20–40% на четыре–восемь недель в затронутых функциях — и укомплектуйте команду поддержки запуска полномочиями менять конфигурацию, а не только регистрировать обращения.",
            ]),

            ("h2", "Сценарий 5: управление меряет активность, а не жизнеспособность"),
            ("p", "Управляющий комитет получает выполнение вех, закрытые обращения, сконфигурированные модули. Всё это может быть зелёным, пока ответ на вопрос «выдержит ли это наш крупнейший рынок на реальном объёме?» ухудшается."),
            ("ul", [
                "<strong>Ранний сигнал:</strong> статусная отчётность стабильно от жёлтой до зелёной, а неформальные разговоры с практиками стабильно пессимистичны.",
                "<strong>Почему игнорируется:</strong> разрыв виден, только если кто-то целенаправленно сравнивает одно с другим, а это ничья задача.",
                "<strong>Контрмера:</strong> один ежеквартальный разговор с практиками без последствий, проводимый вне отчётной вертикали человеком с достаточными полномочиями. Самая дешёвая система раннего предупреждения — и её почти никогда не используют.",
            ]),
            ("q", "К моменту, когда статус становится красным, информация, из-за которой он должен был покраснеть, обычно доступна уже два квартала."),

            ("h2", "Сценарий 6: тестирование счастливого пути на удобном объёме"),
            ("p", "Тестирование подтверждает, что система делает то, что написано в проекте, на чистых данных, при комфортном объёме, на пилотном рынке. Продуктив не является ничем из перечисленного."),
            ("ul", [
                "<strong>Ранний сигнал:</strong> нагрузочный тест на пиковом историческом объёме не проводился; сценарии исключений задокументированы, но не выполнены.",
                "<strong>Почему игнорируется:</strong> тест на пиковом объёме требует данных и инфраструктуры уровня продуктива, а это дорого и легко отложить.",
                "<strong>Контрмера:</strong> возьмите самый нагруженный рынок или период в вашей истории и докажите систему там до принятия обязательств. Пилоты на малых рынках доказывают управляемость изменениями, а не пропускную способность, — именно здесь доработанная архитектура Lidl упёрлась в потолок.",
            ]),

            ("h2", "Сценарий 7: слишком раннее отключение запасного варианта"),
            ("p", "Унаследованную систему выключают или перестают синхронизировать до того, как новая отработала полный бизнес-цикл на полном объёме. Провал проекта превращается в операционный кризис без пути назад."),
            ("ul", [
                "<strong>Ранний сигнал:</strong> нет письменной протестированной процедуры отката или прежняя система перестала получать данные.",
                "<strong>Почему игнорируется:</strong> держать две системы дорого, и это ощущается как неуверенность.",
                "<strong>Контрмера:</strong> сохраняйте запасной вариант работоспособным минимум один полный бизнес-цикл — закрытие месяца, квартала, пиковый сезон — и один раз реально протестируйте откат. Возможность вернуться на прежнюю систему — главная причина, по которой списание €500 млн у Lidl не стало ещё хуже.",
            ]),

            ("h2", "Чек-лист перед запуском"),
            ("p", "Ничего из этого не требует новых инструментов. На всё можно ответить «да» или «нет» за одно заседание управляющего комитета."),
            ("checklist", [
                "Существует единый реестр постоянных отклонений от стандарта с названным владельцем по каждому пункту.",
                "Стоимость накатывания двух следующих мажорных релизов вендора оценена и принята.",
                "Запуск не назначен на пиковый торговый период, и исключённые кварталы объявлены заранее.",
                "У каждого домена данных есть бизнес-владелец, подписавший пороги качества.",
                "Проведено минимум две полнообъёмные репетиции миграции со сверкой с источником.",
                "Нагрузочный тест выполнен на пиковом историческом объёме, а не на удобном.",
                "Сценарии исключений выполнены, а не только описаны.",
                "Заложено падение производительности, есть команда поддержки запуска с правом менять конфигурацию.",
                "Существует письменная процедура отката, и она один раз протестирована.",
                "Прежняя система останется работоспособной минимум один полный бизнес-цикл.",
                "Письменные критерии остановки для следующей вехи согласованы до наступления даты.",
                "В этом квартале состоялся разговор с практиками без последствий, вне отчётной вертикали.",
            ]),

            ("h2", "Если вы уже внутри такого проекта"),
            ("steps", [
                ("Отделите жизнеспособность от активности в отчёте этой недели",
                 "Задайте один вопрос, на который статусный отчёт не отвечает: какие есть доказательства, что это выдержит наш крупнейший рынок на реальном объёме? Если ответ — план, а не результат теста, вот ваша позиция."),
                ("Соберите реестр отклонений на одну страницу",
                 "Если его нет, сборка займёт два дня и обычно это самый информативный документ, который вообще производится на программе."),
                ("Напишите критерии остановки для следующей вехи прямо сейчас",
                 "Конкретные, измеримые, согласованные до наступления даты. Критерии, написанные после срыва, — это переговоры."),
                ("Защитите запасной вариант",
                 "Что бы ни решили, сохраняйте способность старой системы работать. Это превращает худший сценарий из кризиса в дорогое разочарование."),
                ("Определите, кому разрешено сказать «стоп»",
                 "Программы становятся отменяемыми, когда прекратить их могут не только те, с кем они отождествляются. Назовите этого человека явно и заранее."),
            ]),
            ("note", "Неудобная закономерность публичной записи: почти каждую из этих программ можно было остановить за долю итоговой стоимости, и почти ни одну не остановили — потому что в каждой отдельной точке решения продолжать было дешевле, чем остановиться."),
        ],
    },
    takeaways={
        "en": [
            "Almost none of the documented ERP disasters were software defects; they were decisions about process, data, timing and governance that the software then executed faithfully.",
            "The deviation register — every permanent difference from standard, with an owner — is the single most informative document on an ERP programme, and usually nobody's job to produce.",
            "Never schedule go-live into a peak trading period; declare the excluded quarters in advance, before a date gets publicly committed.",
            "Data migration is a business exercise in deciding what records mean; give each data domain a business owner and run two full-volume rehearsals.",
            "Budget an explicit 20–40% productivity dip for four to eight weeks, and give hypercare authority to change configuration rather than only log tickets.",
            "Keep the legacy system viable through one full business cycle and test the rollback once for real — that's what turns a catastrophe into an expensive disappointment.",
        ],
        "ru": [
            "Почти ни один из задокументированных провалов ERP не был дефектом ПО: это были решения о процессах, данных, сроках и управлении, которые система добросовестно исполнила.",
            "Реестр отклонений — каждое постоянное отличие от стандарта с владельцем — самый информативный документ на ERP-программе, и обычно его никто не обязан вести.",
            "Никогда не назначайте запуск на пиковый торговый период; объявите исключённые кварталы заранее, до публичных обязательств по дате.",
            "Миграция данных — это бизнес-упражнение по определению смысла записей; дайте каждому домену бизнес-владельца и проведите две полнообъёмные репетиции.",
            "Заложите явное падение производительности на 20–40% на четыре–восемь недель и дайте команде поддержки запуска право менять конфигурацию, а не только регистрировать обращения.",
            "Держите прежнюю систему работоспособной один полный бизнес-цикл и один раз реально протестируйте откат — именно это превращает катастрофу в дорогое разочарование.",
        ],
    },
    faq={
        "en": [
            ("What is the most common reason ERP implementations fail?",
             "Customising the product to preserve an existing process instead of changing the process. Each deviation looks individually justified, but together they create a permanent branch that makes every future upgrade more expensive and removes the vendor's reference behaviour as a source of truth."),
            ("How early can an ERP failure be detected?",
             "Usually two to four quarters before it appears in status reporting. The reliable early signals are a growing deviation register touching core data models, scope being cut in test phases rather than build phases, no peak-volume performance test, and a persistent gap between green status reports and pessimistic practitioner conversations."),
            ("Why is data migration such a common failure point?",
             "Because it is scoped as a technical transfer when it is really a business exercise in deciding what records mean — which duplicates are the same customer, which prices are still valid, which codes are dead. Without a business owner per data domain signing off on quality thresholds, those decisions get made implicitly by whoever writes the migration script."),
            ("Should we go live big-bang or phased?",
             "Either can work; what matters more is whether the fallback stays viable through a full business cycle and whether a tested rollback procedure exists. Big-bang without a rollback is the configuration that turns a project failure into an operational crisis."),
            ("How much productivity loss should we plan for after go-live?",
             "As a planning assumption, 20–40% in affected functions for four to eight weeks. Plans that assume a return to baseline within days are the ones that generate the workarounds and shadow processes that outlive the project."),
            ("What single practice most reduces the risk?",
             "Written kill criteria agreed before each milestone: a specific, measurable condition under which the programme stops. Almost every documented failure could have been stopped for a fraction of its final cost, and almost none were, because continuing was always locally cheaper than stopping."),
        ],
        "ru": [
            ("Какая самая частая причина провала внедрений ERP?",
             "Доработка продукта ради сохранения существующего процесса вместо изменения процесса. Каждое отклонение по отдельности выглядит обоснованным, но вместе они создают постоянную ветку, которая удорожает каждое будущее обновление и лишает вас эталонного поведения вендора как источника истины."),
            ("Насколько рано можно обнаружить провал ERP?",
             "Обычно за два-четыре квартала до того, как он проявится в отчётности. Надёжные ранние сигналы: растущий реестр отклонений, затрагивающий базовые модели данных; сокращение объёма на фазах тестирования, а не разработки; отсутствие нагрузочного теста на пиковом объёме; устойчивый разрыв между зелёными отчётами и пессимистичными разговорами с практиками."),
            ("Почему миграция данных так часто становится точкой отказа?",
             "Потому что её описывают как технический перенос, тогда как это бизнес-упражнение по определению смысла записей: какие дубли — один клиент, какие цены ещё действуют, какие коды мертвы. Без бизнес-владельца по каждому домену, подписывающего пороги качества, эти решения неявно принимает тот, кто пишет скрипт миграции."),
            ("Запускаться разом или поэтапно?",
             "Работать может и то и другое; важнее, остаётся ли запасной вариант работоспособным на протяжении полного бизнес-цикла и есть ли протестированная процедура отката. Единовременный запуск без отката — та самая конфигурация, которая превращает провал проекта в операционный кризис."),
            ("Какое падение производительности закладывать после запуска?",
             "В качестве планового допущения — 20–40% в затронутых функциях на четыре–восемь недель. Планы, предполагающие возврат к норме за несколько дней, и порождают обходные пути и теневые процессы, переживающие проект."),
            ("Какая одна практика сильнее всего снижает риск?",
             "Письменные критерии остановки, согласованные до каждой вехи: конкретное измеримое условие, при котором программа прекращается. Почти каждый задокументированный провал можно было остановить за долю итоговой стоимости, и почти ни один не остановили, потому что продолжать всегда было локально дешевле."),
        ],
    },
)
