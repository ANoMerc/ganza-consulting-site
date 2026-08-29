# -*- coding: utf-8 -*-
"""Чек-лист «нанимать или автоматизировать». Выжимка из одноимённой статьи."""
BLOCKS = {
    "ru": [
        ("p", "Одностраничный чек-лист к статье <a href=\"{{BLOG}}automation-instead-of-hiring/\">"
              "автоматизация вместо найма</a>. Заполняется за час, до разговора с подрядчиком "
              "и до открытия вакансии."),

        ("h2", "Шаг 1. Посчитайте сотрудника целиком"),
        ("p", "Оклад — видимая часть. Умножьте на коэффициенты и получите годовую цифру."),
        ("table", {
            "caption": "Полная стоимость сотрудника",
            "head": ["Строка", "Ориентир", "Ваша цифра"],
            "rows": [
                ["Годовой оклад", "база", ""],
                ["Налоги и взносы работодателя", "+20–40%, зависит от юрисдикции", ""],
                ["Рабочее место, техника, лицензии", "+5–15% в год", ""],
                ["Выход на производительность", "1–3 месяца оклада, однократно", ""],
                ["Время руководителя", "2–6 часов в неделю", ""],
                ["Риск неудачного найма", "20–40% попыток", ""],
                ["ИТОГО в год", "обычно 1,5–2 оклада", ""],
            ],
        }),
        ("note", "Отдельно посчитайте календарь: от решения «нанимаем» до самостоятельной "
                 "работы обычно проходит 3–5 месяцев. Если задача горит, это часть цены."),

        ("h2", "Шаг 2. Посчитайте автоматизацию целиком"),
        ("table", {
            "caption": "Полная стоимость автоматизации, на три года",
            "head": ["Строка", "Ориентир", "Ваша цифра"],
            "rows": [
                ["Стоимость сборки", "база", ""],
                ["Поддержка при изменениях смежных систем", "10–20% в год, бессрочно", ""],
                ["Обработка исключений", "может превысить сборку", ""],
                ["Проверка корректности результата", "регулярно", ""],
                ["ИТОГО за 3 года", "", ""],
            ],
        }),

        ("h2", "Шаг 3. Разделите работу"),
        ("checklist", [
            "Работа описана шагами, а не должностью.",
            "Каждый шаг помечен как рутина или решение.",
            "Часы посчитаны отдельно по каждой группе.",
            "Видно, что решений мало по времени и много по риску.",
        ]),

        ("h2", "Шаг 4. Проверьте рутинную часть"),
        ("checklist", [
            "Процесс будет таким же через 18 месяцев.",
            "Два человека описывают его одинаково.",
            "Доля исключений ниже 20%.",
            "Кто-то смотрит на результат и заметит ошибку.",
            "Процесс был бы нужен и в хорошо устроенной компании.",
        ]),
        ("p", "Хотя бы один невыполненный пункт — сначала переделка процесса."),

        ("h2", "Шаг 5. Проверьте на ответственность"),
        ("checklist", [
            "У результата шага есть адресат, с которого можно спросить.",
            "Понятно, что произойдёт при неверном результате и кто это заметит.",
            "Этот человек не станет подписываться под выводом, не проверив его.",
        ]),
        ("q", "Если станет — вы автоматизировали не работу, а снятие ответственности."),

        ("h2", "Когда ответ — «нанять»"),
        ("checklist", [
            "Работа не повторяется: каждый раз новая форма задачи.",
            "Вы нанимаете человека, который сам уберёт свою рутину.",
            "Компания маленькая, объёма повторов не хватает окупить поддержку.",
        ]),
        ("p", "Вопрос на собеседовании, который отсеивает лучше остальных: <strong>что вы "
              "автоматизировали на прошлом месте и что из этого сломалось.</strong>"),
    ],
    "en": [
        ("p", "A one-page checklist for the article <a href=\"{{BLOG}}automation-instead-of-hiring/\">"
              "automate or hire</a>. It takes an hour, and it happens before you talk to a "
              "supplier and before you open a vacancy."),

        ("h2", "Step 1. Cost the employee in full"),
        ("p", "Salary is the visible part. Apply the multipliers and get the annual figure."),
        ("table", {
            "caption": "Full cost of an employee",
            "head": ["Line", "Reference point", "Your figure"],
            "rows": [
                ["Annual salary", "base", ""],
                ["Employer taxes and contributions", "+20–40%, jurisdiction-dependent", ""],
                ["Workspace, equipment, licences", "+5–15% per year", ""],
                ["Ramp to productivity", "1–3 months of salary, once", ""],
                ["Manager's time", "2–6 hours per week", ""],
                ["Risk of a bad hire", "20–40% of attempts", ""],
                ["TOTAL per year", "usually 1.5–2× salary", ""],
            ],
        }),
        ("note", "Cost the calendar separately: from deciding to hire to working unsupervised is "
                 "usually 3–5 months. If the problem is urgent, that is part of the price."),

        ("h2", "Step 2. Cost the automation in full"),
        ("table", {
            "caption": "Full cost of automation, over three years",
            "head": ["Line", "Reference point", "Your figure"],
            "rows": [
                ["Build cost", "base", ""],
                ["Maintenance when neighbouring systems change", "10–20% per year, indefinitely", ""],
                ["Exception handling", "can exceed the build", ""],
                ["Checking the output is still correct", "recurring", ""],
                ["TOTAL over 3 years", "", ""],
            ],
        }),

        ("h2", "Step 3. Split the work"),
        ("checklist", [
            "The work is described as steps, not as a job title.",
            "Every step is tagged routine or decision.",
            "Hours are counted separately for each group.",
            "It is visible that decisions are small in time and large in risk.",
        ]),

        ("h2", "Step 4. Test the routine part"),
        ("checklist", [
            "The process will be materially the same in 18 months.",
            "Two people describe it identically.",
            "The exception rate is below 20%.",
            "Somebody looks at the output and would notice an error.",
            "The process would be needed even in a well-run version of the company.",
        ]),
        ("p", "Any single line unchecked means redesign the process first."),

        ("h2", "Step 5. Test for accountability"),
        ("checklist", [
            "The output of the step has an addressee who can be held to it.",
            "It is clear what happens if the output is wrong and who would notice.",
            "That person would not sign off on the conclusion without checking it.",
        ]),
        ("q", "If they would, you haven't automated the work — you've automated the removal of accountability."),

        ("h2", "When the answer is \"hire\""),
        ("checklist", [
            "The work doesn't repeat: a different shape every time.",
            "You are hiring someone who will remove their own routine.",
            "The company is small and there isn't enough repetition to pay back maintenance.",
        ]),
        ("p", "The interview question that filters best: <strong>what did you automate in your "
              "last job, and what part of it broke.</strong>"),
    ],
}
