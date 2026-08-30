# -*- coding: utf-8 -*-
"""Шумовой аудит по Канеману.

Источник — «Шум. Несовершенство человеческих суждений» (Канеман, Сибони,
Санстейн, 2021) и протокол промежуточных оценок Канемана и Сибони. Здесь это
переложено на решения, которые принимает небольшая компания: наём, оценка
подрядчика, приоритеты, сметы.

Связан со статьями про найм как фильтр (шум в собеседованиях) и про тихий
отказ (независимая оценка до обсуждения).
"""
BLOCKS = {
    "ru": [
        ("p", "Когда решение оказывается неверным, обычно ищут предвзятость: посмотрели не на "
              "то, поддались первому впечатлению, испугались рисковать. Предвзятость — "
              "systematic отклонение, среднее промахивается в одну сторону, и её хотя бы "
              "можно заметить."),
        ("p", "Есть вторая половина ошибки, которую почти никогда не измеряют. Это "
              "<strong>шум</strong> — разброс в решениях, которые должны были совпасть. Два "
              "человека смотрят на одно и то же и приходят к разным выводам. Или один человек "
              "в понедельник и в четверг."),
        ("q", "Общая ошибка = предвзятость² + шум². Уменьшать можно любую половину, а измеряют "
              "обычно только первую."),
        ("p", "Разница на практике важнее, чем кажется. Ошибки от предвзятости накапливаются в "
              "одну сторону и рано или поздно становятся заметны. Ошибки от шума <em>не "
              "компенсируют друг друга</em>: завышенная смета одному клиенту не отменяет "
              "заниженную другому — это два разных клиента и два разных ущерба."),
        ("note", "В страховой компании из книги пять одинаковых дел раздали разным андеррайтерам. "
                 "Медианный разброс котировок составил 55%: один и тот же клиент мог получить "
                 "9 500 или 16 700 долларов в зависимости от того, кому попало его дело. "
                 "Руководство до аудита ожидало разброса около 10%."),

        ("h2", "Где искать шум у себя"),
        ("p", "Шум живёт там, где решение принимается человеком, повторяется и не имеет "
              "мгновенной обратной связи. В небольшой компании это обычно:"),
        ("ul", [
            "оценка кандидата на собеседовании;",
            "оценка сметы или сроков по новой задаче;",
            "приоритет заявки, тикета или инцидента;",
            "оценка качества работы подрядчика;",
            "решение «берём или не берём» по проекту;",
            "оценка риска перед запуском.",
        ]),
        ("p", "Общий признак: если бы это решение принимал другой человек из вашей команды, "
              "результат мог бы отличаться — и вы никогда не узнаете, потому что второй раз "
              "то же дело никто не рассматривает."),

        ("h2", "Три вида шума — их лечат по-разному"),
        ("table", {
            "caption": "Из чего складывается системный шум",
            "head": ["Вид", "Как выглядит", "Что с этим делать"],
            "rows": [
                ["Уровневый",
                 "Один человек систематически строже или щедрее остальных: у него всегда выше смета или ниже оценка кандидата",
                 "Общая шкала с якорями и сверка средних между оценщиками"],
                ["Устойчивый ситуативный",
                 "Человек стабильно реагирует на определённый признак: на опыт в конкретной отрасли, на аккуратное резюме, на знакомый стек",
                 "Разбить решение на независимые оценки, чтобы признак не окрашивал всё сразу"],
                ["Случайный",
                 "Тот же человек, то же дело, другой день — другой вывод. Настроение, усталость, порядок рассмотрения, погода",
                 "Усреднение нескольких независимых оценок; решение не в конце тяжёлого дня"],
            ],
        }),

        ("h2", "Как провести шумовой аудит"),
        ("p", "Занимает один день и даёт цифру, которой у вас сейчас нет. Проводить стоит до "
              "того, как чинить процесс: без замера непонятно, есть ли что чинить."),
        ("steps", [
            ("Возьмите 4–6 реальных дел",
             "Настоящих, из прошлого, с настоящими материалами. Выдуманные кейсы дают выдуманный разброс: люди чувствуют учебную задачу и стараются больше обычного."),
            ("Раздайте их всем, кто такие решения принимает",
             "Минимум трое. Каждый оценивает все дела самостоятельно и не обсуждает ни с кем — это условие, без которого замер бессмысленен."),
            ("Попросите число, а не мнение",
             "Смета в деньгах, срок в неделях, оценка кандидата по шкале, вероятность в процентах. Словесная оценка не измеряется."),
            ("Соберите и посчитайте разброс",
             "По каждому делу: минимум, максимум, медиана. Главная цифра — во сколько раз максимум больше минимума."),
            ("Спросите заранее, какого разброса они ожидают",
             "Задайте этот вопрос до того, как покажете результат. Разрыв между ожиданием и фактом обычно и есть самое убедительное в аудите."),
            ("Разберите крайние случаи вместе",
             "Не для того чтобы найти виноватого, а чтобы понять, на что смотрели те, кто дал минимум и максимум. Почти всегда выясняется, что они оценивали разные вещи."),
        ]),
        ("note", "Аудит меряет <strong>согласованность</strong>, а не правоту. Даже если "
                 "правильный ответ неизвестен и появится через год, разброс виден сегодня. "
                 "В этом и ценность: шум можно измерить, не зная истины."),

        ("h2", "Гигиена решений: шесть приёмов"),
        ("p", "Из книги, в порядке отношения пользы к усилиям для небольшой команды."),
        ("checklist", [
            "<strong>Разбейте решение на независимые оценки.</strong> Вместо «нравится или нет» — три-четыре отдельных вопроса, каждый со своей шкалой. Общее впечатление собирается в конце, из них.",
            "<strong>Оценивайте до обсуждения, а не после.</strong> Каждый пишет своё число молча. Озвученное первым мнение стягивает на себя остальные, и вы получаете одно мнение вместо трёх.",
            "<strong>Усредняйте независимые оценки.</strong> Среднее трёх независимых суждений почти всегда точнее лучшего из них — при условии, что они действительно независимы.",
            "<strong>Сравнивайте, а не оценивайте в вакууме.</strong> «Этот кандидат сильнее или слабее того, кого мы взяли в марте» надёжнее, чем «оцените от 1 до 10».",
            "<strong>Возьмите внешнюю точку зрения.</strong> Сколько такие задачи занимали у нас раньше? Что говорит статистика по отрасли? Базовая величина до собственной оценки, а не после.",
            "<strong>Задайте порядок поступления информации.</strong> Сведения, которые не нужны для конкретной оценки, до неё не показывайте: они окрасят всё остальное.",
        ]),
        ("q", "Интуицию не запрещают — её откладывают. Целостное суждение выносится после "
              "того, как сделаны отдельные оценки, а не вместо них."),

        ("h2", "Протокол промежуточных оценок"),
        ("p", "Готовая процедура Канемана и Сибони для решений, которые стоят дорого: наём "
              "ключевого человека, выбор подрядчика, крупная смета, запуск направления."),
        ("steps", [
            ("Разложите решение на 3–5 независимых оценок",
             "Они должны быть по возможности не связаны друг с другом. Для подрядчика, например: понимание задачи, техническая состоятельность, прозрачность цены, риск непрерывности."),
            ("Для каждой найдите внешнюю точку отсчёта",
             "С чем сравниваем: прошлые проекты, рыночные ориентиры, ваши же завершённые случаи."),
            ("Назначьте разных людей на разные оценки",
             "Если людей мало, разнесите оценки по времени, чтобы одна не тянула за собой другую."),
            ("На встрече разберите оценки по очереди, не переходя к выводу",
             "Сначала все узнают все оценки. Итоговое суждение — только после этого."),
            ("Оценка — разговор — переоценка",
             "Каждый молча ставит своё число, потом общий разговор, потом каждый молча ставит число заново. Расхождение после второго круга и есть настоящее разногласие."),
            ("Не усредняйте механически",
             "Финальное решение принимает человек, а не таблица. Смысл протокола в том, чтобы он принимал его, увидев картину целиком."),
        ]),

        ("h2", "Чего этот подход стоит"),
        ("p", "Честно, потому что без этого раздела получится реклама метода."),
        ("ul", [
            "Решения станут медленнее. Независимые оценки требуют времени, которого при «давайте быстро обсудим» не тратят.",
            "Часть людей воспримет это как недоверие. Помогает объяснить, что меряется процесс, а не человек, и начать с аудита, где виноватых нет по устройству.",
            "Дробление подходит не всему. Решение, которое принимается раз в жизни и не повторяется, дробить незачем: шум измеряется только на повторяющихся суждениях.",
            "Формальность может создать ложную уверенность. Структурированная оценка выглядит объективной — а это ровно тот эффект, из-за которого показанный ход рассуждения повышает доверие быстрее, чем точность.",
        ]),
        ("p", "Последний пункт стоит держать в голове отдельно: он разобран в статье про "
              "<a href=\"{{BLOG}}hiring-as-a-filter/\">найм как фильтр</a>, где та же механика "
              "мешает изменить подбор на уровне софта."),

        ("h2", "С чего начать завтра"),
        ("p", "Одно упражнение, которое почти ничего не стоит и обычно меняет разговор. "
              "Возьмите последнюю задачу, которую оценивали по срокам. Попросите двух коллег "
              "независимо назвать свою оценку в неделях, не показывая им вашу и не давая им "
              "увидеть оценку друг друга."),
        ("p", "Если разброс окажется в полтора-два раза — у вас нормальный человеческий шум и "
              "стоит завести правило независимых оценок. Если больше — вы оцениваете не одну "
              "и ту же задачу, и это уже не про шум, а про постановку."),
    ],

    "en": [
        ("p", "When a decision turns out wrong, people look for bias: we looked at the wrong "
              "thing, anchored on a first impression, were too cautious. Bias is a systematic "
              "deviation — the average misses in one direction — and at least it can be spotted."),
        ("p", "There is a second half of the error that almost nobody measures. It is "
              "<strong>noise</strong> — scatter in judgements that should have agreed. Two "
              "people look at the same thing and reach different conclusions. Or one person on "
              "Monday and on Thursday."),
        ("q", "Overall error = bias² + noise². Either half can be reduced; usually only the "
              "first is ever measured."),
        ("p", "The practical difference matters more than it sounds. Bias errors accumulate in "
              "one direction and eventually become visible. Noise errors <em>do not cancel "
              "out</em>: an overpriced quote to one client doesn't offset an underpriced one to "
              "another — those are two different clients and two separate harms."),
        ("note", "In the insurance company from the book, five identical cases were handed to "
                 "different underwriters. The median spread in quotes was 55%: the same client "
                 "could be quoted $9,500 or $16,700 depending on whose desk the case landed on. "
                 "Before the audit, management expected a spread of about 10%."),

        ("h2", "Where to look for noise in your own work"),
        ("p", "Noise lives wherever a judgement is made by a person, repeats, and has no "
              "immediate feedback. In a small company that usually means:"),
        ("ul", [
            "assessing a candidate in an interview;",
            "estimating cost or duration for a new task;",
            "prioritising a request, ticket or incident;",
            "judging the quality of a supplier's work;",
            "deciding whether to take a project on;",
            "assessing risk before a launch.",
        ]),
        ("p", "The common marker: if somebody else on your team made this call, the answer might "
              "differ — and you will never find out, because nobody looks at the same case twice."),

        ("h2", "Three kinds of noise, treated differently"),
        ("table", {
            "caption": "What system noise is made of",
            "head": ["Kind", "How it looks", "What to do about it"],
            "rows": [
                ["Level noise",
                 "One person is consistently stricter or more generous: their estimates are always higher, their candidate scores always lower",
                 "A shared scale with anchors, and comparing averages between assessors"],
                ["Stable pattern noise",
                 "A person reliably reacts to one attribute: industry experience, a tidy CV, a familiar stack",
                 "Break the decision into independent assessments so one attribute can't colour everything"],
                ["Occasion noise",
                 "Same person, same case, different day, different answer. Mood, tiredness, the order cases were reviewed, the weather",
                 "Average several independent judgements; don't decide at the end of a hard day"],
            ],
        }),

        ("h2", "How to run a noise audit"),
        ("p", "It takes a day and produces a number you don't currently have. Run it before "
              "fixing anything: without the measurement you don't know whether there is anything "
              "to fix."),
        ("steps", [
            ("Take 4–6 real cases",
             "Real ones, from the past, with the actual materials. Invented cases produce invented scatter: people sense a training exercise and try harder than usual."),
            ("Give them to everyone who makes this kind of call",
             "Three people minimum. Each assesses every case alone and discusses with nobody — without that condition the measurement is meaningless."),
            ("Ask for a number, not an opinion",
             "A price, a duration in weeks, a candidate score, a probability. A verbal assessment cannot be measured."),
            ("Collect the answers and compute the spread",
             "Per case: minimum, maximum, median. The headline figure is how many times larger the maximum is than the minimum."),
            ("Ask in advance what spread they expect",
             "Put that question before you show the result. The gap between expectation and fact is usually the most persuasive part of the audit."),
            ("Discuss the extremes together",
             "Not to find someone to blame, but to understand what the person at the minimum and the person at the maximum were each looking at. Almost always they were assessing different things."),
        ]),
        ("note", "The audit measures <strong>agreement</strong>, not correctness. Even when the "
                 "right answer is unknown and won't be known for a year, the scatter is visible "
                 "today. That is the point: noise can be measured without knowing the truth."),

        ("h2", "Decision hygiene: six practices"),
        ("p", "From the book, ordered by value-to-effort for a small team."),
        ("checklist", [
            "<strong>Break the decision into independent assessments.</strong> Instead of \"do we like it\", three or four separate questions, each with its own scale. The overall impression is assembled at the end, out of those.",
            "<strong>Assess before discussing, not after.</strong> Everyone writes their number in silence. The first opinion spoken pulls the others toward it, and you end up with one opinion instead of three.",
            "<strong>Average independent judgements.</strong> The average of three independent assessments is almost always better than the best one of them — provided they really were independent.",
            "<strong>Compare rather than score in a vacuum.</strong> \"Is this candidate stronger or weaker than the one we hired in March\" is more reliable than \"rate them 1 to 10\".",
            "<strong>Take the outside view.</strong> How long did tasks like this take us before? What does the industry data say? The base rate goes before your own estimate, not after.",
            "<strong>Sequence the information.</strong> Anything not needed for a particular assessment shouldn't be shown before it: it will colour everything else.",
        ]),
        ("q", "Intuition isn't banned — it is delayed. The holistic judgement comes after the "
              "separate assessments, not instead of them."),

        ("h2", "The mediating assessments protocol"),
        ("p", "Kahneman and Sibony's ready-made procedure for expensive decisions: hiring a key "
              "person, choosing a supplier, a large estimate, launching a line of business."),
        ("steps", [
            ("Break the decision into 3–5 independent assessments",
             "As unrelated to each other as possible. For a supplier, for instance: grasp of the problem, technical soundness, price transparency, continuity risk."),
            ("Find an outside reference point for each",
             "What are we comparing against: past projects, market benchmarks, your own completed cases."),
            ("Assign different people to different assessments",
             "If there aren't enough people, separate the assessments in time so one doesn't drag the next along."),
            ("In the meeting, review the assessments one at a time without concluding",
             "First everyone learns all the assessments. The overall judgement comes only after that."),
            ("Estimate, talk, estimate again",
             "Each person silently records a number, then the group discusses, then each records a number again in silence. Disagreement after the second round is real disagreement."),
            ("Don't average mechanically",
             "The final call is made by a person, not a spreadsheet. The point of the protocol is that they make it having seen the whole picture."),
        ]),

        ("h2", "What this approach costs"),
        ("p", "Honestly, because without this section it reads as an advert for a method."),
        ("ul", [
            "Decisions get slower. Independent assessments take time that \"let's just talk it through quickly\" doesn't spend.",
            "Some people will read it as distrust. It helps to explain that the process is being measured rather than the person, and to start with the audit, where by construction nobody is at fault.",
            "Not everything should be broken up. A decision made once and never repeated doesn't need decomposing: noise is only measurable on recurring judgements.",
            "Formality can create false confidence. A structured assessment looks objective — and that is exactly the effect by which showing the reasoning raises trust faster than accuracy does.",
        ]),
        ("p", "That last point deserves separate attention: it is worked through in "
              "<a href=\"{{BLOG}}hiring-as-a-filter/\">hiring as a filter</a>, where the same "
              "mechanism prevents recruitment from being fixed at the software level."),

        ("h2", "Where to start tomorrow"),
        ("p", "One exercise that costs almost nothing and usually changes the conversation. Take "
              "the last task you estimated for duration. Ask two colleagues to name their own "
              "estimate in weeks, independently, without seeing yours or each other's."),
        ("p", "A spread of one and a half to two times is ordinary human noise, and it is worth "
              "adopting a rule of independent estimates. More than that and you are not "
              "estimating the same task — which is no longer about noise, but about how the "
              "task was framed."),
    ],
}
