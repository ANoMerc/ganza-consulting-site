# -*- coding: utf-8 -*-
CASE = dict(
    order=2,
    accent="blue",
    client={"en": "Logistics and international trade · up to 50 people · 2025",
            "ru": "Логистика и международная торговля · до 50 человек · 2025"},
    stat={"en": "−60% routine", "ru": "−60% рутины"},
    title={"en": "AI manager instead of a hire", "ru": "ИИ-менеджер вместо найма"},
    problem={
        "en": "The owner wanted to hire another manager, then decided AI should do the job "
              "instead: estimates, documents and bookkeeping, mail triage, logistics "
              "suggestions. The question on the table was which of those a model could "
              "actually be trusted with.",
        "ru": "Владелец собирался нанять ещё одного менеджера, а потом решил, что вместо "
              "человека справится ИИ: сметы, документы и бухгалтерия, разбор почты, "
              "предложения по логистике. Вопрос на столе был один — что из этого модели "
              "действительно можно доверить.",
    },
    did={
        "en": "Six CustDev interviews with the managers, accountants and lawyers who do the "
              "work. The conclusion was that paid AI models were the wrong tool here: data "
              "leakage, hallucinations in documents that carry legal weight, nobody to hold "
              "responsible for an answer, a pull toward the standard solution when the case "
              "was not standard, running cost, geographic restrictions and an internet "
              "connection that drops. So the routine went into an n8n workflow with "
              "templates and spreadsheets, and a Telegram bot took over mail handling and "
              "internal comms.",
        "ru": "Шесть интервью CustDev с менеджерами, бухгалтерами и юристами — с теми, кто "
              "эту работу делает. Вывод: платные ИИ-модели здесь не тот инструмент — утечки "
              "данных, галлюцинации в документах, у которых есть юридический вес, "
              "отсутствие ответственного за ответ, склонность выдавать стандартное решение "
              "там, где случай нестандартный, стоимость, географические ограничения и "
              "перебои со связью. Поэтому рутина уехала в процессы на n8n с шаблонами и "
              "таблицами, а Telegram-бот взял на себя разбор почты и внутреннюю "
              "коммуникацию.",
    },
    result={"en": "−60% time on routine and −40% on mail triage, measured together over "
                  "two months of running the new process",
            "ru": "−60% времени на рутину и −40% на разбор почты — замер общий, за два "
                  "месяца работы нового процесса"},
    honest={
        "en": "The numbers come from the team's own before-and-after estimate over two "
              "months, not from instrumented time tracking — treat them as the order of "
              "magnitude, not a measurement. Worth saying plainly: nothing here went wrong. "
              "Weekly calls, written minutes, edits where they were needed. The interesting "
              "part of this case is the answer, not the drama.",
        "ru": "Цифры — оценка самой команды до и после, за два месяца, а не хронометраж. "
              "Это порядок величины, а не измерение. И честно: в этом проекте ничего не "
              "ломалось. Созвоны раз в неделю, письменные протоколы, правки там, где были "
              "нужны. Интересен здесь ответ, а не драма.",
    },
    tags=["n8n", "Telegram", "CustDev", "Operations"],
)
