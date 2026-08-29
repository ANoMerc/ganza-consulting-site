# -*- coding: utf-8 -*-
"""Чек-лист выбора подрядчика. Из «Как выбрать консультанта» и «Студии из одного человека»."""
BLOCKS = {
    "ru": [
        ("p", "Список вопросов, которые стоит задать до подписания, и то, как звучит хороший "
              "и плохой ответ на каждый. Развёрнутые версии — в статьях "
              "<a href=\"{{BLOG}}how-to-choose-a-consultant/\">как выбрать бизнес-консультанта</a> и "
              "<a href=\"{{BLOG}}one-person-consulting-studio/\">студия из одного человека</a>."),

        ("h2", "Пять вопросов любому подрядчику"),
        ("table", {
            "caption": "Что спрашивать и что слушать в ответе",
            "head": ["Вопрос", "Хороший ответ", "Плохой ответ"],
            "rows": [
                ["Кто именно делает работу и есть ли этот человек на созвоне?",
                 "Имена и доля их времени на вашем проекте",
                 "«Команда», «наши специалисты», уклонение от чисел"],
                ["Сколько клиентов будет параллельно с моим?",
                 "Конкретное число, любое",
                 "Уклонение — сигнал важнее самого числа"],
                ["Что заставило бы вас отговорить меня от этого проекта?",
                 "Названный сценарий, при котором браться не стоит",
                 "«У нас всё получится» — продают деятельность"],
                ["Что остаётся у меня в конце и в каком виде?",
                 "Модели, данные, скрипты, логика решений в редактируемом виде",
                 "PDF и презентация — это не владение"],
                ["Что будет, если исполнитель станет недоступен?",
                 "Конкретика: где лежит работа, как часто промежуточные результаты",
                 "«Всё будет нормально»"],
            ],
        }),

        ("h2", "Четыре гарантии непрерывности"),
        ("p", "Требуйте их у любого подрядчика, но особенно у маленького. Отсутствие ответа "
              "хуже, чем неудобный ответ."),
        ("checklist", [
            "<strong>Работа лежит там, где вы её достанете.</strong> В ваших системах или общем репозитории с первого дня, а не отдаётся в конце.",
            "<strong>Промежуточный результат с фиксированной частотой.</strong> Раз в одну-две недели что-то, что можно посмотреть. Это ограничивает вашу уязвимость длиной цикла, а не длиной проекта.",
            "<strong>Названный запасной исполнитель.</strong> Конкретный человек или компания, названные заранее. Честное «его нет» лучше обещания кого-нибудь найти.",
            "<strong>Письменные условия на случай недоступности.</strong> Что происходит со сроком и деньгами, если подрядчик пропал. Согласовано до старта.",
        ]),
        ("note", "Задайте большой компании эквивалентный вопрос: «если человек, которого вы "
                 "ставите на проект, уйдёт, что изменится для меня и кто мне об этом скажет?» "
                 "Ответ часто менее конкретен, чем у хорошего одиночки."),

        ("h2", "Признаки раздутого объёма"),
        ("checklist", [
            "Первый этап называется «погружение» и занимает больше двух недель.",
            "В предложении есть работы, которых нет в вашей постановке.",
            "Цена названа за период, а не за результат, и период открытый.",
            "На вопрос «что будет на выходе» отвечают форматом, а не содержанием.",
            "Нет ни одного пункта, от которого подрядчик предложил бы отказаться.",
        ]),

        ("h2", "Перед подписанием"),
        ("checklist", [
            "Объём зафиксирован письменно: что входит, что не входит, к какой дате.",
            "Названы признаки, по которым обе стороны поймут, что получилось.",
            "Понятно, кто с вашей стороны принимает решения и отвечает в течение дня.",
            "NDA подписан до передачи данных, а не после.",
            "Понятно, что произойдёт при сдвиге срока — с обеих сторон.",
        ]),
    ],
    "en": [
        ("p", "The questions worth asking before you sign, and what a good and a bad answer to "
              "each sounds like. Longer versions in "
              "<a href=\"{{BLOG}}how-to-choose-a-consultant/\">how to choose a consultant</a> and "
              "<a href=\"{{BLOG}}one-person-consulting-studio/\">the one-person studio</a>."),

        ("h2", "Five questions for any supplier"),
        ("table", {
            "caption": "What to ask and what to listen for",
            "head": ["Question", "Good answer", "Bad answer"],
            "rows": [
                ["Who exactly does the work, and are they on this call?",
                 "Names, and what share of their time you get",
                 "\"The team\", \"our specialists\", evasion on numbers"],
                ["How many clients will run alongside mine?",
                 "A specific number, any number",
                 "Evasion — the signal matters more than the number"],
                ["What would make you talk me out of this project?",
                 "A named scenario in which they'd decline",
                 "\"It'll be fine\" — they're selling activity"],
                ["What do I keep at the end, and in what form?",
                 "Models, data, scripts, decision logic, editable",
                 "A PDF and a deck are not ownership"],
                ["What happens if the person becomes unavailable?",
                 "Specifics: where the work lives, how often interim results arrive",
                 "\"Everything will be fine\""],
            ],
        }),

        ("h2", "Four continuity guarantees"),
        ("p", "Demand these from any supplier, and especially from a small one. No answer is "
              "worse than an uncomfortable answer."),
        ("checklist", [
            "<strong>The work sits where you can reach it.</strong> In your systems or a shared repository from day one, not handed over at the end.",
            "<strong>Interim results at a fixed cadence.</strong> Something reviewable every one to two weeks. That caps your exposure at one cycle, not the length of the project.",
            "<strong>A named backup.</strong> A specific person or company, named in advance. An honest \"there isn't one\" beats a promise to find somebody.",
            "<strong>Written terms for unavailability.</strong> What happens to the deadline and the money if the supplier disappears. Agreed before the start.",
        ]),
        ("note", "Ask a large firm the equivalent question: \"if the person you put on this "
                 "project leaves, what changes for me and who tells me?\" The answer is often "
                 "less specific than a good solo supplier's."),

        ("h2", "Signs of inflated scope"),
        ("checklist", [
            "The first stage is called \"immersion\" and runs longer than two weeks.",
            "The proposal contains work that isn't in your brief.",
            "The price is per period rather than per result, and the period is open-ended.",
            "\"What will we get\" is answered with a format rather than content.",
            "There isn't a single item the supplier suggested dropping.",
        ]),

        ("h2", "Before signing"),
        ("checklist", [
            "Scope is fixed in writing: what's in, what's out, by when.",
            "The criteria by which both sides will know it worked are named.",
            "It is clear who on your side decides and answers within a day.",
            "The NDA is signed before data is handed over, not after.",
            "It is clear what happens if the deadline moves — on either side.",
        ]),
    ],
}
