# -*- coding: utf-8 -*-
"""Протокол решения. Из поста про асинхронные команды + «Тихий отказ» + LeSS."""
BLOCKS = {
    "ru": [
        ("p", "Встреча без записи, которую потом видят все, порождает один и тот же набор "
              "реплик: «вы этого не говорили», «вы сказали иначе», «я не слышал», «вы все не "
              "так поняли». Спорить с этим бессмысленно — надо убрать причину."),
        ("p", "Протокол решает три вопроса и ничего больше: <strong>кто что сказал, кому что "
              "поручено, что решено</strong>. Задачи уходят на доску, все остаются в курсе."),
        ("note", "Правило, из которого всё остальное следует: встречи без записи, доступной "
                 "всем участникам, не должно быть. Если запись некому вести — значит, встреча "
                 "могла быть сообщением."),

        ("h2", "Шапка"),
        ("checklist", [
            "Дата и повод: что именно обсуждали, одной строкой.",
            "Кто был. Кого не было, но решение его касается — важнее первого.",
            "Ссылка на предыдущий протокол по этой теме, если он есть.",
        ]),

        ("h2", "Решения"),
        ("p", "Главный раздел. Одно решение — одна строка. Формулировка в прошедшем времени и "
              "без модальностей: «решили», а не «договорились подумать»."),
        ("table", {
            "caption": "Что фиксировать по каждому решению",
            "head": ["Решение", "Почему так", "Кто принял", "Как оспорить"],
            "rows": [["", "", "", ""], ["", "", "", ""]],
        }),
        ("p", "Колонка «почему так» — та, ради которой протокол вообще стоит вести. Через "
              "полгода решение будет выглядеть произвольным, если рядом нет причины. Колонка "
              "«как оспорить» отвечает на вопрос, который иначе задают в коридоре: что делать "
              "тому, кто не согласен."),
        ("q", "Разработчику обычно не нужна встреча. Нужно знать, что решили, почему и куда "
              "идти, если с этим не согласен."),

        ("h2", "Задачи"),
        ("checklist", [
            "Формулировка задачи так, как она попадёт на доску.",
            "Один исполнитель. Не отдел, не «команда» — имя.",
            "Срок или явная пометка, что срока нет и почему.",
            "От чего задача зависит и кто это разблокирует.",
        ]),

        ("h2", "Открытые вопросы"),
        ("p", "Раздел, который чаще всего пропускают. Вопрос без ответа — это не пустое место, "
              "а работа, которую кто-то должен сделать."),
        ("checklist", [
            "Формулировка вопроса.",
            "Кому адресован.",
            "К какому моменту нужен ответ и что встанет без него.",
        ]),

        ("h2", "Что считается сделанным"),
        ("p", "Приём из Large-Scale Scrum, полезный далеко за пределами разработки. Запишите "
              "условия, при которых обсуждённое считается завершённым, — и отдельно то, что в "
              "эти условия не вошло, но всё равно должно произойти:"),
        ("q", "Отгружаемое = определение готовности + недоделанная работа."),
        ("p", "Смысл второго списка в том, что невключённая работа никуда не девается. Она не "
              "запланирована, накапливается невидимо и всплывает тогда, когда исправлять "
              "дороже всего."),

        ("h2", "Блокеры и риски"),
        ("p", "Ставьте этот раздел выше статусов, а на встрече спрашивайте о нём первым. "
              "Порядок пунктов задаёт, что считается содержанием разговора: если первым "
              "спрашивают статус, статусом всё и закончится."),
        ("checklist", [
            "Что мешает прямо сейчас.",
            "Какие решения выглядят хрупкими — даже если формально приняты.",
            "Мелочи, которые повторяются третий раз подряд. Это ранние признаки, а не шум.",
        ]),

        ("h2", "Как это работает в асинхронной команде"),
        ("steps", [
            ("Появляется задача",
             "В общем канале, а не в личке: личка — это решение, о котором остальные не узнают."),
            ("У типа задачи есть ответственный специалист",
             "Задача уходит к нему. Если ответственного нет, это первый открытый вопрос протокола."),
            ("Он запрашивает декомпозицию, если она нужна",
             "Отказ от декомпозиции — тоже решение, и его тоже стоит записать."),
            ("Организационную часть берёт на себя автоматизация",
             "Фиксация решений, обновление задач, назначение ответственных, сроки, переадресация открытых вопросов тем, кто может ответить. Похожие схемы давно работают в строительстве, чтобы прораб не тонул в бумагах."),
            ("Контекст меняется — все уведомлены",
             "Не «есть новый протокол», а что именно изменилось и кого это касается."),
        ]),
        ("note", "Честное предупреждение: при таком порядке принятие решений становится более "
                 "плавным и одновременно более долгим. Это плата за то, что контекст переживает "
                 "разговор. Если решение нужно немедленно — созвонитесь, но запись всё равно "
                 "оставьте."),

        ("h2", "Раз в квартал — общий разбор"),
        ("p", "Отдельная практика, которую стоит забрать из LeSS: ретроспектива не команды, а "
              "системы. Разбирают не то, как прошёл спринт у одной группы, а то, что "
              "повторяется между группами и почему организация раз за разом наступает на "
              "одно и то же."),
        ("checklist", [
            "Какие вопросы из протоколов остались открытыми дольше квартала.",
            "Какие решения пришлось пересматривать и что мы не знали в момент принятия.",
            "Какие мелочи повторились больше трёх раз.",
            "Что из недоделанной работы накопилось и когда мы её закроем.",
        ]),
    ],

    "en": [
        ("p", "A meeting with no record that everyone can see afterwards produces the same set "
              "of lines every time: \"you didn't say that\", \"you said it differently\", \"I "
              "didn't hear that\", \"you all misunderstood\". Arguing with that is pointless — "
              "remove the cause instead."),
        ("p", "A decision record answers three questions and nothing else: <strong>who said "
              "what, who was given which task, what was decided</strong>. Tasks go to the "
              "board, everyone stays informed."),
        ("note", "The rule everything else follows from: a meeting without a record visible to "
                 "its participants shouldn't happen. If there is nobody to keep the record, the "
                 "meeting could have been a message."),

        ("h2", "Header"),
        ("checklist", [
            "Date and occasion: what was discussed, in one line.",
            "Who attended. Who didn't but is affected by the decision — more important than the first.",
            "A link to the previous record on this subject, if there is one.",
        ]),

        ("h2", "Decisions"),
        ("p", "The main section. One decision, one row. Past tense, no modals: \"decided\", not "
              "\"agreed to think about\"."),
        ("table", {
            "caption": "What to capture for each decision",
            "head": ["Decision", "Why this way", "Who decided", "How to challenge it"],
            "rows": [["", "", "", ""], ["", "", "", ""]],
        }),
        ("p", "The \"why this way\" column is the reason to keep a record at all. Six months "
              "later the decision will look arbitrary without a reason beside it. The \"how to "
              "challenge it\" column answers the question otherwise asked in the corridor: what "
              "should someone who disagrees do?"),
        ("q", "A developer usually doesn't need the meeting. They need to know what was decided, "
              "why, and where to go if they disagree."),

        ("h2", "Tasks"),
        ("checklist", [
            "The task worded as it will appear on the board.",
            "One assignee. Not a department, not \"the team\" — a name.",
            "A date, or an explicit note that there is none and why.",
            "What the task depends on, and who unblocks it.",
        ]),

        ("h2", "Open questions"),
        ("p", "The section most often skipped. An unanswered question isn't an empty space — it "
              "is work somebody has to do."),
        ("checklist", [
            "The question, worded.",
            "Who it is addressed to.",
            "By when an answer is needed and what stalls without it.",
        ]),

        ("h2", "What counts as done"),
        ("p", "A practice from Large-Scale Scrum that is useful well beyond software. Write down "
              "the conditions under which what was discussed counts as finished — and separately "
              "what didn't make that list but still has to happen:"),
        ("q", "Potentially shippable = definition of done + undone work."),
        ("p", "The point of the second list is that excluded work doesn't disappear. It is "
              "unplanned, accumulates invisibly, and surfaces when fixing it costs the most."),

        ("h2", "Blockers and risks"),
        ("p", "Put this section above statuses, and ask about it first in the meeting. The order "
              "of items defines what counts as the content of the conversation: ask for status "
              "first and status is what you get."),
        ("checklist", [
            "What is in the way right now.",
            "Which decisions look fragile — even ones formally made.",
            "Small things recurring for the third time. Those are early signals, not noise.",
        ]),

        ("h2", "How this runs in an asynchronous team"),
        ("steps", [
            ("A task appears",
             "In a shared channel, not a direct message: a DM is a decision the rest never learn about."),
            ("There is a specialist responsible for this type of task",
             "The task goes to them. If there is no such person, that is the record's first open question."),
            ("They request decomposition if it is needed",
             "Declining to decompose is also a decision, and worth recording too."),
            ("Automation handles the organisational part",
             "Recording decisions, updating tasks, assigning responsibility, setting deadlines, forwarding open questions to whoever can answer them. Similar setups have long been used in construction to keep site supervisors out of paperwork."),
            ("The context changes and everyone is notified",
             "Not \"there is a new record\" but what changed and who it affects."),
        ]),
        ("note", "An honest warning: with this arrangement decision-making becomes more fluid "
                 "and simultaneously more prolonged. That is the price of context outliving the "
                 "conversation. If a decision is needed now, get on a call — but still leave the "
                 "record."),

        ("h2", "Once a quarter: an overall review"),
        ("p", "A separate practice worth taking from LeSS: a retrospective of the system rather "
              "than of a team. It examines not how one group's sprint went but what repeats "
              "between groups, and why the organisation keeps stepping on the same thing."),
        ("checklist", [
            "Which questions from the records stayed open longer than a quarter.",
            "Which decisions had to be revisited, and what we didn't know when we made them.",
            "Which small things recurred more than three times.",
            "How much undone work has accumulated, and when we will clear it.",
        ]),
    ],
}
