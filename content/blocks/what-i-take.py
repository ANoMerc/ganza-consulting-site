# -*- coding: utf-8 -*-
"""«За что я берусь и за что нет».

Страница, которой нет ни у кого на этом рынке, — и это единственная причина,
по которой она работает. Отказ без объяснения читается как каприз, поэтому у
каждого пункта написано, почему именно так, а не «мы отбираем клиентов».
"""
BLOCKS = {
    "ru": [
        ("p", "Обычно подрядчик перечисляет, что умеет, и молчит о том, за что не "
              "возьмётся. Узнать это можно только на третьем созвоне, когда время уже "
              "потрачено — ваше и моё. Поэтому вот список заранее."),
        ("p", "Он не про сложность. За сложное я как раз берусь: в этом смысл формата "
              "<a href=\"{{SERVICES}}#pricing\">«Там, где чек-лист заканчивается»</a>. "
              "Он про условия, при которых работа не даст результата, сколько бы её ни "
              "было."),

        ("h2", "За что берусь"),
        ("ul", [
            "<strong>Задача сформулирована как вопрос, а не как желание.</strong> "
            "«Почему промо-акции перестали окупаться» — вопрос. «Сделайте нам хорошо» — нет.",
            "<strong>У задачи есть владелец на вашей стороне.</strong> Один человек, "
            "который принимает решения и может ответить в течение дня.",
            "<strong>Есть данные или доступ к ним.</strong> Пусть разрозненные, пусть "
            "в выгрузках — но существующие.",
            "<strong>Результат можно проверить.</strong> До старта понятно, по какому "
            "признаку мы поймём, что получилось.",
        ]),

        ("h2", "За что не берусь"),

        ("h3", "1. Задача без владельца"),
        ("p", "Если на вопрос «кто принимает решение по этой задаче» ответа нет или их "
              "три, работа превращается в согласование мнений. Я могу собрать данные, "
              "посчитать и написать вывод — и он ляжет в папку, потому что внедрять его "
              "некому. Это не проблема мотивации, это отсутствие адресата."),
        ("p", "<strong>Что делать:</strong> назначьте владельца до того, как искать "
              "подрядчика. Даже если это вы сами и у вас нет времени — тогда честнее "
              "перенести задачу на квартал, когда время будет."),

        ("h3", "2. Владелец, который сегодня один, а завтра другой"),
        ("p", "Смена ответственного в середине проекта обнуляет контекст. Новый человек "
              "не участвовал в решениях, не согласен с половиной из них и справедливо "
              "хочет начать сначала. Дважды пройденный путь никто не оплачивает, а "
              "результат всё равно выходит хуже: он собран из компромиссов между двумя "
              "разными представлениями о задаче."),
        ("p", "<strong>Что делать:</strong> если вы знаете, что ответственный меняется "
              "или уходит — дождитесь. Двух недель ожидания дешевле, чем два месяца "
              "работы вхолостую."),

        ("h3", "3. «Подтвердите наше решение»"),
        ("p", "Иногда решение уже принято, а нужен внешний человек, чтобы его "
              "легитимизировать перед советом директоров, инвестором или партнёром. "
              "Это понятная задача, но не моя: я не знаю заранее, к какому выводу приду, "
              "и не могу обещать нужный. Если я соглашусь и приду к другому — вы "
              "заплатили за проблему, а не за её решение."),
        ("p", "<strong>Что делать:</strong> если вам действительно нужна проверка "
              "решения, а не его подтверждение, так и напишите. Это <a "
              "href=\"{{SERVICES}}#pricing\">точечная экспертиза</a>, и она стоит "
              "недорого. Но с готовностью услышать «нет»."),

        ("h3", "4. Нет времени на подготовку"),
        ("p", "«Нужно к пятнице» почти всегда означает, что на сбор данных, разговор с "
              "теми, кто делает работу руками, и проверку гипотез времени нет. Тогда "
              "остаётся выдать правдоподобное мнение, а правдоподобное мнение стоит "
              "ровно ноль: у вас оно и так есть, причём бесплатно."),
        ("p", "<strong>Что делать:</strong> если срок жёсткий и сдвинуть его нельзя, "
              "уменьшите вопрос. Один узкий вопрос за неделю лучше, чем широкий за ту "
              "же неделю."),

        ("h2", "Что ещё я не делаю"),
        ("p", "Короче и без объяснений, потому что тут всё очевидно: продвижение и "
              "реклама, дизайн как отдельная услуга, мобильные приложения, поддержка "
              "чужого кода на постоянной основе, найм и оценка персонала."),

        ("h2", "Если вы всё-таки напишете"),
        ("p", "Ничего страшного не произойдёт. Первый разговор бесплатный, и если задача "
              "из списка выше, я скажу это в первые двадцать минут, а не через месяц. "
              "Когда у меня есть релевантный контакт — назову, к кому идти. Если нет, "
              "скажу и это: выдумывать рекомендацию, за которую я не отвечаю, "
              "бессмысленно."),
        ("note", "Смысл этой страницы простой. Отказ на входе стоит одного разговора. "
                 "Отказ на середине проекта стоит денег, времени и осадка — обоим."),
    ],

    "en": [
        ("p", "Suppliers usually list what they can do and stay quiet about what they "
              "won't take on. You find that out on the third call, once the time has "
              "already been spent — yours and mine. So here is the list up front."),
        ("p", "It isn't about difficulty. Difficult is the point of the "
              "<a href=\"{{SERVICES}}#pricing\">\"Where the checklist runs out\"</a> "
              "format. It is about the conditions under which no amount of work "
              "produces a result."),

        ("h2", "What I take on"),
        ("ul", [
            "<strong>The problem is phrased as a question, not a wish.</strong> "
            "\"Why did our promotions stop paying for themselves\" is a question. "
            "\"Make things good\" is not.",
            "<strong>The problem has an owner on your side.</strong> One person who "
            "makes decisions and can answer within a day.",
            "<strong>Data exists, or access to it does.</strong> Scattered is fine, "
            "raw exports are fine — existing is the requirement.",
            "<strong>The result can be checked.</strong> Before we start, it is clear "
            "how we will know it worked.",
        ]),

        ("h2", "What I decline"),

        ("h3", "1. A problem with no owner"),
        ("p", "If \"who decides on this\" has no answer, or three of them, the work "
              "turns into reconciling opinions. I can gather the data, do the "
              "arithmetic and write the conclusion — and it will sit in a folder, "
              "because there is nobody to implement it. That is not a motivation "
              "problem; there is simply no addressee."),
        ("p", "<strong>What to do:</strong> appoint an owner before looking for a "
              "supplier. Even if that is you and you have no time — then it is more "
              "honest to move the work to a quarter when you do."),

        ("h3", "2. An owner who changes mid-project"),
        ("p", "Replacing the responsible person halfway resets the context. The new one "
              "wasn't part of the decisions, disagrees with half of them, and quite "
              "reasonably wants to start again. Nobody pays for the same road twice, "
              "and the result is worse anyway: it ends up assembled from compromises "
              "between two different views of the problem."),
        ("p", "<strong>What to do:</strong> if you know the owner is changing or "
              "leaving, wait. Two weeks of waiting is cheaper than two months of work "
              "that goes nowhere."),

        ("h3", "3. \"Confirm the decision we've already made\""),
        ("p", "Sometimes the decision is made and an outside name is needed to "
              "legitimise it in front of a board, an investor or a partner. That is a "
              "real need, but not mine to serve: I don't know in advance what I will "
              "conclude, and I can't promise the conclusion you want. If I agree and "
              "then reach a different one, you have paid for a problem rather than a "
              "solution."),
        ("p", "<strong>What to do:</strong> if you genuinely want the decision tested "
              "rather than endorsed, say so. That is "
              "<a href=\"{{SERVICES}}#pricing\">pinpoint expertise</a> and it is "
              "inexpensive — but it comes with the possibility of hearing no."),

        ("h3", "4. No time to prepare"),
        ("p", "\"We need it by Friday\" almost always means there is no time to gather "
              "data, talk to the people who do the work, or test a hypothesis. What is "
              "left is producing a plausible opinion, and a plausible opinion is worth "
              "exactly nothing: you already have one, for free."),
        ("p", "<strong>What to do:</strong> if the deadline is genuinely fixed, shrink "
              "the question. One narrow question in a week beats a broad one in the "
              "same week."),

        ("h2", "Other things I don't do"),
        ("p", "Shorter, and without explanation, because these are obvious: marketing "
              "and advertising, design as a standalone service, mobile apps, ongoing "
              "maintenance of someone else's codebase, hiring and staff assessment."),

        ("h2", "If you write anyway"),
        ("p", "Nothing bad happens. The first conversation is free, and if the problem "
              "is on the list above I'll say so in the first twenty minutes rather than "
              "a month in. Where I have a relevant contact, I'll tell you who to talk "
              "to. Where I don't, I'll say that too: inventing a referral I can't stand "
              "behind helps nobody."),
        ("note", "The point of this page is simple. Saying no at the start costs one "
                 "conversation. Saying no halfway through costs money, time and "
                 "goodwill — on both sides."),
    ],
}
