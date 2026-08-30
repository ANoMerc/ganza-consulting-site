# -*- coding: utf-8 -*-
POST = dict(
    slug="hiring-as-a-filter",
    date="2026-09-29",
    updated="2026-09-29",
    tag={"en": "Hiring", "ru": "Найм"},
    title={
        "en": "Hiring as a Filter: Why a High Bar Selects the Wrong People",
        "ru": "Найм как фильтр: почему высокий порог отбирает не тех",
    },
    h1={
        "en": "Hiring as a Filter: Why Raising the Bar Selects the Wrong People",
        "ru": "Найм как фильтр: почему высокий порог входа отбирает не тех",
    },
    dek={
        "en": "The harder you make it to get in, the more reliably you select people who are excellent at getting in — which is a different skill from doing the job.",
        "ru": "Чем труднее попасть внутрь, тем надёжнее вы отбираете тех, кто отлично проходит собеседования. А это другой навык, чем делать работу.",
    },
    description={
        "en": "The paradox of raising the bar, why hiring software makes it worse rather than better, and what to compete on instead.",
        "ru": "Парадокс высокого порога, почему софт для найма делает хуже, а не лучше, и в чём стоит соревноваться вместо этого.",
    },
    keywords={
        "en": "hiring process problems, interview filters, employee retention vs hiring, internal mobility, recruitment automation risks, candidate screening bias",
        "ru": "проблемы найма, фильтры на собеседовании, удержание вместо найма, внутренняя мобильность, автоматизация подбора риски, отбор кандидатов",
    },
    hashtags=["Hiring", "Retention", "Management", "AI", "Operations"],
    related=["automation-instead-of-hiring", "informal-org-structures", "infrastructure-inbreeding"],
    body={
        "ru": [
            ("p", "Про кризис найма сейчас говорят много. Собеседования становятся длиннее, "
                  "тестовые задания — объёмнее, этапов отбора всё больше. Обсуждают обычно "
                  "одно: как тяжело стало попасть в компанию."),
            ("p", "Вопрос, который при этом теряется, интереснее: <strong>почему компании "
                  "соревнуются именно в том, чтобы вход был труднее?</strong>"),

            ("h2", "Мысленный эксперимент"),
            ("p", "Возьмём двух специалистов с одинаковым опытом и одинаковыми способностями."),
            ("p", "Первый работает в компаниях с развитой внутренней мобильностью: он может "
                  "переходить между командами, продуктами, функциями и ролями, не увольняясь. "
                  "Второй — в компаниях с жёсткими внутренними границами: чтобы вырасти, ему "
                  "нужно менять работодателя."),
            ("p", "Через пять лет второй, скорее всего, сменил несколько компаний и вышел на "
                  "более высокую зарплату или должность. Первый может всё ещё работать там же, "
                  "спокойно продвигаясь по внутренним траекториям."),
            ("q", "С точки зрения работодателя тип карьерной траектории не главное. Главное — "
                  "способен ли человек стабильно давать результат и держать ответственность."),
            ("p", "Такие люди есть в обеих группах. Проблема начинается не здесь, а в тот "
                  "момент, когда компания строит стратегию найма вокруг максимально высокого "
                  "порога входа."),

            ("h2", "Парадокс высокого порога"),
            ("p", "Чем труднее попасть внутрь, тем надёжнее организация отбирает тех, кто "
                  "исключительно хорош в прохождении собеседований. Это измеримый, тренируемый "
                  "и вполне реальный навык — просто не тот, за который платят потом."),
            ("p", "Хуже другое. Специалисты, которые регулярно проходят отборы, становятся "
                  "великолепны в смене работодателя. И тогда получается вот что:"),
            ("ul", [
                "компания усложняет найм, чтобы снизить риск ошибки;",
                "усложнение отбирает тех, кто лучше всех проходит фильтры;",
                "те же люди лучше всех проходят фильтры и в следующий раз;",
                "риск не снизился, он переехал из найма в удержание.",
            ]),
            ("note", "Это не аргумент за то, чтобы брать всех подряд. Это аргумент за то, чтобы "
                     "понимать, какой именно навык вы измеряете, и не путать его с тем, который "
                     "вам нужен."),

            ("h2", "Почему софт делает хуже, а не лучше"),
            ("p", "Мы разрабатывали систему, которая оценивает кандидатов по косвенным признакам, "
                  "и по ходу упёрлись в вывод, который перечеркнул исходную идею: "
                  "<strong>изменить современный найм на уровне программы невозможно</strong>."),
            ("p", "Причина не в качестве алгоритма. Рекрутер делегирует программе собственное "
                  "суждение. В такой ситуации улучшать алгоритм бессмысленно — меняется не "
                  "решение, а его источник."),
            ("p", "И есть эффект, который окончательно закрывает эту дверь. Если показать "
                  "человеку, <em>как именно</em> программа пришла к выводу, он согласится с "
                  "выводом ещё сильнее, а не начнёт его проверять."),
            ("q", "Объяснимость повышает доверие быстрее, чем точность. Человек, которому "
                  "показали ход рассуждения, перестаёт проверять результат."),
            ("p", "Фильтры на агрегаторах вакансий работают ровно так уже сейчас, просто проще. "
                  "Добавление ИИ не отменяет механизм, а усиливает его: чем убедительнее "
                  "объяснение, тем меньше остаётся надзора."),
            ("p", "Из того же наблюдения следует и более общая граница, разобранная в статье "
                  "<a href=\"../automation-instead-of-hiring/\">автоматизация вместо найма</a>: "
                  "решение, за которое кто-то отвечает лично, автоматизируется до состояния "
                  "«подготовлено», но не «принято». Машина не может нести ответственность, а без "
                  "ответственности нет гарантий."),

            ("h2", "Что происходит, если фильтр всё-таки ошибся"),
            ("p", "Ошибка найма обнаруживается быстро — если в компании работают каналы связи, "
                  "адаптация и обратная связь. Расхождение между ожиданиями и реальностью "
                  "становится видно за недели, а не за кварталы."),
            ("p", "И вот тут проявляется связь с тем, о чём говорилось в статье про "
                  "<a href=\"../silent-failure-mode/\">тихий отказ</a>: в организации, где "
                  "неудобные сигналы не имеют канала, ошибка найма всплывает поздно и дорого. "
                  "Тогда единственным способом снизить риск действительно кажется фильтр на "
                  "входе — и цикл замыкается."),
            ("table", {
                "caption": "Две стратегии снижения риска ошибки найма",
                "head": ["", "Фильтр на входе", "Быстрая проверка внутри"],
                "rows": [
                    ["Что измеряется", "Умение проходить отбор", "Умение делать работу"],
                    ["Когда виден результат", "Через несколько месяцев", "Через несколько недель"],
                    ["Цена ошибки", "Оплаченный период плюс повторный найм", "Стажировка или испытательный проект"],
                    ["Побочный эффект", "Отбор мастеров смены работодателя", "Нужны работающие каналы обратной связи"],
                    ["Что усиливается со временем", "Порог растёт, поток сужается", "Организация учится быстрее видеть"],
                ],
            }),
            ("p", "Если каналы работают, разумнее пускать больше людей в стажировки, "
                  "испытательные периоды и пробные проекты и принимать решение по фактической "
                  "работе, а не по результату собеседования."),

            ("h2", "Соседний риск: закрытый контур"),
            ("p", "У противоположной крайности есть своя цена. Компания, которая растит "
                  "руководителей только изнутри, постепенно теряет разнообразие взглядов: новые "
                  "идеи начинают восприниматься как угроза устоявшимся практикам, а внешние "
                  "кандидаты — как чужаки. Подробно этот механизм разобран в статье про "
                  "<a href=\"../infrastructure-inbreeding/\">инфраструктурный инбридинг</a>."),
            ("p", "То есть выбор не между «высокий порог» и «низкий порог». Обе крайности "
                  "воспроизводят себя: первая отбирает по навыку прохождения фильтра, вторая — "
                  "по совпадению с уже имеющимся управленческим контуром."),

            ("h2", "Вопросы, которые стоит задавать в обе стороны"),
            ("p", "Полезное свойство этой темы в том, что проверить компанию можно теми же "
                  "вопросами, которыми она проверяет вас. Вот те, что дают больше всего "
                  "информации, — и то, что стоит услышать в ответе."),
            ("steps", [
                ("«Если через месяц станет ясно, что я не справился, — что именно я сделал или не сделал?»",
                 "Нужны конкретные признаки провала. «Не подошёл по культуре» почти всегда означает, что ожидания не сформулированы."),
                ("«Кто имеет право сказать «нет» новой инициативе и как расставляются приоритеты?»",
                 "«Мы стараемся делать всё» — это операционный хаос, переодетый в амбицию."),
                ("«Расскажите про случай, когда команда хотела автономии, а бизнесу нужен был контроль»",
                 "«Мы просто доверяем людям» без механизмов ответственности — тревожный признак, а не достоинство."),
                ("«Когда ваш процесс в последний раз не прижился и почему?»",
                 "Если ответ «люди не следовали» — зрелость процессов, скорее всего, низкая."),
                ("«Как стратегия превращается в операционный план?»",
                 "Должна быть видна цепочка: стратегия → цели → дорожная карта → бэклог → показатели. Без неё команды гребут в разные стороны."),
            ]),
            ("p", "Эти вопросы не ищут идеальную компанию. Они ищут разрыв между красивыми "
                  "словами про автономию и тем, как в организации на самом деле принимаются "
                  "решения."),

            ("h2", "В чём стоит соревноваться"),
            ("p", "Сильные организации выигрывают не тем, что не пускают внутрь. Они выигрывают "
                  "тем, что быстро понимают, кто подходит, дают возможности расти и удерживают "
                  "ценных людей дольше конкурентов."),
            ("q", "Многие до сих пор соревнуются в том, кто поставит на входную дверь замок "
                  "надёжнее. Настоящий вопрос — кто научится строить дом, из которого не хочется "
                  "уходить."),
            ("p", "Если фильтр всё-таки нужен, его стоит хотя бы измерить: <a href=\"{{HOME}}templates/noise-audit/\">шумовой аудит</a> за день показывает, насколько расходятся оценки разных интервьюеров по одним и тем же кандидатам. Обычно сильнее, чем ожидают."),
        ],

        "en": [
            ("p", "There is a great deal of talk about the hiring crisis. Interviews get longer, "
                  "take-home assignments get heavier, the number of screening stages keeps "
                  "growing. The discussion is usually about one thing: how hard it has become "
                  "to get into a company."),
            ("p", "The question that gets lost is more interesting: <strong>why are companies "
                  "competing to make entry harder in the first place?</strong>"),

            ("h2", "A thought experiment"),
            ("p", "Take two professionals with the same experience and the same capability."),
            ("p", "The first works in companies with strong internal mobility: they can move "
                  "between teams, products, functions and roles without leaving. The second "
                  "works in companies with rigid internal boundaries: to grow, they have to "
                  "change employer."),
            ("p", "Five years later the second has probably worked for several companies and "
                  "reached a higher salary or title. The first may still be in the same "
                  "organisation, progressing steadily through internal paths."),
            ("q", "From an employer's perspective the shape of the career is not what matters. "
                  "What matters is whether the person consistently delivers and carries the "
                  "responsibility handed to them."),
            ("p", "Such people exist in both groups. The problem doesn't start here. It starts "
                  "when a company builds its hiring strategy around the highest possible "
                  "barrier to entry."),

            ("h2", "The paradox of the high bar"),
            ("p", "The harder it is to get in, the more reliably the organisation selects people "
                  "who are exceptionally good at passing interviews. That is a measurable, "
                  "trainable and entirely real skill — it just isn't the one being paid for "
                  "afterwards."),
            ("p", "Worse: professionals who regularly go through hiring processes become "
                  "excellent at changing employers. Which produces this:"),
            ("ul", [
                "the company makes hiring harder to reduce risk;",
                "the difficulty selects for people who pass filters best;",
                "the same people also pass filters best next time;",
                "the risk didn't fall — it moved from hiring to retention.",
            ]),
            ("note", "This is not an argument for hiring anyone who applies. It is an argument "
                     "for knowing which skill you are measuring and not confusing it with the "
                     "one you need."),

            ("h2", "Why software makes it worse, not better"),
            ("p", "We were building a system that assesses candidates from indirect signals, and "
                  "along the way ran into a conclusion that cancelled the original idea: "
                  "<strong>modern hiring cannot be changed at the software level</strong>."),
            ("p", "Not because of algorithm quality. The recruiter delegates their own judgement "
                  "to the software. In that situation improving the algorithm is beside the "
                  "point — what changed isn't the decision but its source."),
            ("p", "And there is an effect that closes the door completely. Show a person "
                  "<em>how</em> the software reached its conclusion and they agree with it more "
                  "strongly, rather than starting to check it."),
            ("q", "Explainability raises trust faster than accuracy. A person shown the "
                  "reasoning stops checking the result."),
            ("p", "Filters on job aggregators already work this way, just more simply. Adding AI "
                  "doesn't remove the mechanism, it strengthens it: the more convincing the "
                  "explanation, the less oversight survives."),
            ("p", "The same observation produces the broader boundary discussed in "
                  "<a href=\"../automation-instead-of-hiring/\">automate or hire</a>: a decision "
                  "somebody answers for personally can be automated to \"prepared\" but not to "
                  "\"made\". A machine cannot carry responsibility, and without responsibility "
                  "there are no guarantees."),

            ("h2", "What happens when the filter gets it wrong"),
            ("p", "A hiring mistake becomes visible quickly — if the company's communication "
                  "channels, onboarding and feedback mechanisms work. The mismatch between "
                  "expectations and reality shows up in weeks, not quarters."),
            ("p", "And here the connection to "
                  "<a href=\"../silent-failure-mode/\">the silent failure mode</a> appears: in an "
                  "organisation where uncomfortable signals have no channel, a hiring mistake "
                  "surfaces late and expensively. At which point a filter at the door genuinely "
                  "does look like the only way to reduce risk — and the loop closes."),
            ("table", {
                "caption": "Two strategies for reducing hiring risk",
                "head": ["", "Filter at the door", "Fast verification inside"],
                "rows": [
                    ["What gets measured", "Skill at passing selection", "Skill at doing the work"],
                    ["When the result is visible", "After several months", "After several weeks"],
                    ["Cost of a mistake", "A paid period plus re-hiring", "An internship or trial project"],
                    ["Side effect", "Selects masters of changing employer", "Requires working feedback channels"],
                    ["What compounds over time", "The bar rises, the pipeline narrows", "The organisation learns to see faster"],
                ],
            }),
            ("p", "If the channels work, it is more effective to let more people into "
                  "internships, probation periods and trial projects, and to decide on actual "
                  "performance rather than interview performance."),

            ("h2", "The neighbouring risk: a closed loop"),
            ("p", "The opposite extreme has its own price. A company that grows leaders only from "
                  "within gradually loses diversity of thought: new ideas start to read as "
                  "threats to established practice, and external candidates as outsiders. That "
                  "mechanism is worked through in "
                  "<a href=\"../infrastructure-inbreeding/\">infrastructure inbreeding</a>."),
            ("p", "So the choice isn't between a high bar and a low one. Both extremes reproduce "
                  "themselves: the first selects for filter-passing skill, the second for "
                  "similarity to the management loop that already exists."),

            ("h2", "Questions worth asking in both directions"),
            ("p", "A useful property of this subject is that you can test a company with the same "
                  "questions it uses to test you. These give the most information — with what to "
                  "listen for in the answer."),
            ("steps", [
                ("\"If in a month it's clear I failed in this role, what exactly would I have done or not done?\"",
                 "You want concrete failure criteria. \"Not a culture fit\" almost always means expectations were never defined."),
                ("\"Who has the authority to say no to a new initiative, and how does prioritisation actually work?\"",
                 "\"We try to do everything\" is operational chaos dressed as ambition."),
                ("\"Tell me about a time the team wanted autonomy and the business needed control.\"",
                 "\"We just trust people\", with no accountability mechanism, is a red flag rather than a virtue."),
                ("\"When did one of your processes last fail to stick, and why?\"",
                 "If the answer is \"people didn't follow it\", process maturity is probably low."),
                ("\"How does strategy become an operational plan?\"",
                 "There should be a visible chain: strategy → objectives → roadmap → backlog → metrics. Without it, teams row in different directions."),
            ]),
            ("p", "These questions aren't looking for a perfect company. They are looking for the "
                  "gap between attractive talk about autonomy and how decisions actually get "
                  "made."),

            ("h2", "What to compete on instead"),
            ("p", "Strong organisations don't win by keeping everyone out. They win by quickly "
                  "identifying who fits, creating room to grow, and retaining valuable people "
                  "longer than their competitors."),
            ("q", "Many are still competing over who fits the sturdier lock to the front door. "
                  "The real question is who learns to build a house people don't want to leave."),
            ("p", "If a filter is genuinely needed, it is worth at least measuring: <a href=\"{{HOME}}templates/noise-audit/\">a noise audit</a> takes a day and shows how far different interviewers diverge on the same candidates. Usually further than anyone expects."),
        ],
    },
    takeaways={
        "ru": [
            "Чем выше порог входа, тем надёжнее компания отбирает тех, кто хорош в прохождении собеседований, а это тренируемый навык, отличный от умения делать работу.",
            "Риск при этом не исчезает, а переезжает из найма в удержание: мастера отбора так же хорошо проходят следующий отбор.",
            "Изменить найм на уровне софта нельзя: рекрутер делегирует программе собственное суждение, и улучшение алгоритма меняет не решение, а его источник.",
            "Объяснимость повышает доверие быстрее точности — человеку показали ход рассуждения, и он перестал проверять результат.",
            "При работающих каналах связи и адаптации ошибка найма видна за недели; тогда стажировки и пробные проекты дешевле высокого порога.",
            "Обратная крайность не лучше: закрытый управленческий контур воспроизводит себя и теряет чувствительность к рынку.",
            "Соревноваться стоит не в высоте порога, а в скорости распознавания подходящих людей и в их удержании.",
        ],
        "en": [
            "The higher the bar, the more reliably a company selects people good at passing interviews — a trainable skill distinct from doing the job.",
            "The risk doesn't disappear, it moves from hiring to retention: masters of selection also pass the next selection.",
            "Hiring cannot be changed at the software level: the recruiter delegates their judgement to the program, so improving the algorithm changes the source of the decision, not the decision.",
            "Explainability raises trust faster than accuracy — shown the reasoning, a person stops checking the result.",
            "With working communication and onboarding, a hiring mistake is visible in weeks; then internships and trial projects cost less than a high bar.",
            "The opposite extreme is no better: a closed leadership loop reproduces itself and loses sensitivity to the market.",
            "The thing worth competing on is not the height of the bar but the speed of recognising who fits, and keeping them.",
        ],
    },
    faq={
        "ru": [
            ("Почему усложнение отбора не снижает риск найма?",
             "Потому что оно измеряет не тот навык. Высокий порог отбирает людей, которые лучше всех проходят собеседования, — это реальное и тренируемое умение, но другое, чем способность давать результат. Те же люди так же успешно проходят следующий отбор, поэтому риск не исчезает, а переезжает из найма в удержание."),
            ("Помогает ли ИИ сделать подбор объективнее?",
             "Скорее наоборот. Рекрутер делегирует программе собственное суждение, поэтому меняется не качество решения, а его источник. Плюс работает эффект объяснимости: когда человеку показывают, как алгоритм пришёл к выводу, он соглашается сильнее и перестаёт проверять. Надзор формально остаётся, фактически отключается."),
            ("Что делать вместо высокого порога входа?",
             "Сокращать время до проверки на реальной работе: стажировки, испытательные периоды, пробные проекты. Это работает при условии, что в компании есть каналы обратной связи и внятная адаптация — тогда расхождение между ожиданиями и реальностью становится видно за недели, а не за кварталы."),
            ("Что лучше — растить своих или брать снаружи?",
             "Обе крайности воспроизводят себя. Ставка только на высокий внешний порог отбирает по навыку прохождения фильтров. Ставка только на внутренний рост постепенно закрывает управленческий контур: новые идеи начинают восприниматься как угроза, а внешние кандидаты — как чужаки. Полезен не выбор одной из крайностей, а осознанная пропорция."),
            ("Как проверить компанию на собеседовании?",
             "Спрашивать про конкретику там, где обычно звучат лозунги. Что именно будет считаться моим провалом через месяц? Кто имеет право сказать «нет» новой инициативе? Когда ваш процесс в последний раз не прижился и почему? Как стратегия превращается в операционный план? Уклончивость в ответах информативнее самих ответов."),
            ("Почему сотрудник, часто менявший работу, — не обязательно проблема?",
             "Потому что траектория чаще говорит об устройстве прежних компаний, чем о человеке. В организации с жёсткими внутренними границами единственный способ вырасти — сменить работодателя. Вопрос, на который стоит отвечать при найме, один: способен ли человек стабильно давать результат и держать ответственность."),
        ],
        "en": [
            ("Why doesn't a harder selection process reduce hiring risk?",
             "Because it measures the wrong skill. A high bar selects people who are best at passing interviews — a real and trainable ability, but a different one from delivering results. Those same people pass the next selection just as successfully, so the risk doesn't disappear; it moves from hiring to retention."),
            ("Does AI make recruitment more objective?",
             "Rather the opposite. The recruiter delegates their own judgement to the software, so what changes is the source of the decision, not its quality. The explainability effect compounds it: shown how the algorithm reached its conclusion, a person agrees more strongly and stops checking. Oversight formally remains and effectively switches off."),
            ("What should replace a high barrier to entry?",
             "Shortening the time to verification on real work: internships, probation periods, trial projects. This works on one condition — that the company has feedback channels and real onboarding. Then the mismatch between expectations and reality becomes visible in weeks rather than quarters."),
            ("Is it better to promote internally or hire externally?",
             "Both extremes reproduce themselves. Betting only on a high external bar selects for filter-passing skill. Betting only on internal growth gradually closes the leadership loop: new ideas read as threats and external candidates as outsiders. What helps is not choosing an extreme but setting the proportion deliberately."),
            ("How do I assess a company during an interview?",
             "Ask for specifics where slogans usually appear. What exactly would count as my failure in a month? Who can say no to a new initiative? When did one of your processes last fail to stick, and why? How does strategy become an operational plan? Evasiveness in the answers is more informative than the answers."),
            ("Why isn't frequent job-changing necessarily a problem?",
             "Because the trajectory usually says more about how previous companies were built than about the person. In an organisation with rigid internal boundaries, changing employer is the only way to grow. The question worth answering when hiring is one: can this person consistently deliver and carry responsibility."),
        ],
    },
)
