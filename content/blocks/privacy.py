# -*- coding: utf-8 -*-
"""Политика конфиденциальности.

Написана под фактическую обработку: что реально собирает analytics.js и что
реально уходит в таблицу leads. Если поменяется код — правится и этот текст,
иначе политика превращается в вымысел, а это ровно то, за что сайт ругает
других. Сроки хранения здесь и в supabase/schema.sql должны совпадать.

ЮРИДИЧЕСКАЯ ПРОВЕРКА: текст написан по закону Грузии «О защите персональных
данных» (в силе с 1 марта 2024) и по GDPR в части экстерриториального
применения. Это не заключение юриста — перед публикацией показать грузинскому
юристу, особенно раздел о международной передаче.
"""
from core import config as cfg

_C = cfg.CONTROLLER


def _who(lang):
    bits = [_C["legal_name"][lang]]
    if _C["reg_number"]:
        bits.append(("идентификационный номер " if lang == "ru" else "registration number ")
                    + _C["reg_number"])
    bits.append(_C["country"][lang])
    if _C["address"]:
        bits.append(_C["address"])
    return ", ".join(bits)


BLOCKS = {
    "ru": [
        ("p", f"Редакция от {_C['updated']}. Этот сайт ведёт "
              f"<strong>{_who('ru')}</strong>. Связаться по любому вопросу из этого "
              f"документа: <a href=\"mailto:{cfg.EMAIL}\">{cfg.EMAIL}</a>."),
        ("note", "Коротко: сайт не ставит cookie, не подключает чужие счётчики и "
                 "не имеет идентификатора, который узнаёт вас в следующий визит. "
                 "Персональные данные появляются только тогда, когда вы сами "
                 "отправляете форму."),

        ("h2", "Что собирается без вашего участия"),
        ("p", "На сайте работает собственная аналитика. Она нужна, чтобы понимать, "
              "какие статьи дочитывают и где люди уходят, — и ничего кроме."),
        ("ul", [
            "адрес страницы, язык версии и заголовок;",
            "источник перехода и UTM-метки, если вы пришли по размеченной ссылке;",
            "тип устройства, операционная система, браузер и размер окна;",
            "клики по ссылкам и кнопкам, глубина прокрутки, время внимания по секциям;",
            "шаги в калькуляторе проекта.",
        ]),
        ("p", "К каждому событию прикладывается <strong>идентификатор сессии</strong> — "
              "случайное число, которое живёт в <code>sessionStorage</code> вашего "
              "браузера и исчезает вместе с вкладкой. Он позволяет собрать один визит "
              "в одну цепочку и не позволяет узнать вас в следующий раз: при повторном "
              "заходе идентификатор будет другим. Межсессионного идентификатора, "
              "cookie и любых рекламных пикселей на сайте нет."),
        ("p", "IP-адрес в аналитике не сохраняется."),

        ("h2", "Что вы отправляете сами"),
        ("p", "Через форму обратной связи вы передаёте имя, способ связи "
              "(почта или телеграм) и текст обращения. Вместе с ними сохраняются "
              "страница, с которой отправлена форма, язык, UTM-метки и идентификатор "
              "сессии — чтобы понимать, откуда пришло обращение."),
        ("p", "Отдельно сохраняется <strong>необратимый хеш вашего IP-адреса</strong> "
              "с секретной солью. Он нужен ровно для одного: ограничить число отправок "
              "с одного источника, чтобы форму не забили спамом. Восстановить из него "
              "IP-адрес нельзя, и ни для чего другого он не используется."),
        ("p", "Основание обработки — ваше согласие, которое вы даёте галочкой под "
              "формой, и мой законный интерес ответить на обращение. Согласие можно "
              "отозвать в любой момент письмом на указанный выше адрес."),

        ("h2", "Где это хранится и кто ещё видит"),
        ("p", "Данные лежат в базе Supabase. Публичный ключ, встроенный в страницу, "
              "умеет только записывать события аналитики и не умеет читать ничего. "
              "Заявки с формы принимает отдельная серверная функция, и записывать "
              "их публичным ключом нельзя. Читать и то и другое может только "
              "авторизованный пользователь — то есть я."),
        ("p", "Обработчики, у которых физически оказываются данные: "
              "<strong>Supabase</strong> (хранение), <strong>Resend</strong> "
              "(доставка письма о новой заявке) и <strong>GitHub Pages</strong> "
              "(отдача самих страниц). Больше никому данные не передаются и никогда "
              "не продаются."),
        ("p", "Серверы этих сервисов находятся за пределами Грузии, поэтому обработка "
              "включает международную передачу данных. Она происходит на основании "
              "вашего согласия и в объёме, необходимом для работы сайта и ответа "
              "на обращение."),

        ("h2", "Сколько это хранится"),
        ("table", {
            "caption": "Сроки хранения. Удаление автоматическое, а не по настроению.",
            "head": ["Что", "Срок", "Что происходит потом"],
            "rows": [
                ["События аналитики", "24 месяца", "Удаляются запланированной задачей в базе"],
                ["Заявки с формы", "36 месяцев", "Удаляются запланированной задачей в базе"],
                ["Хеш IP-адреса", "вместе с заявкой", "Удаляется в том же цикле"],
                ["Переписка по почте и в телеграме", "пока нужна для работы", "Удаляется по вашему запросу"],
            ],
        }),

        ("h2", "Ваши права"),
        ("p", "По закону Грузии «О защите персональных данных» вы можете:"),
        ("ul", [
            "узнать, обрабатываются ли ваши данные, и получить их копию;",
            "потребовать исправить неточные данные;",
            "потребовать удалить данные или прекратить обработку;",
            "отозвать согласие — после этого обработка прекращается;",
            "подать жалобу в надзорный орган Грузии.",
        ]),
        ("p", f"Чтобы воспользоваться любым из них, напишите на "
              f"<a href=\"mailto:{cfg.EMAIL}\">{cfg.EMAIL}</a>. Отвечаю в сроки, "
              f"установленные законом; если для ответа нужно вас идентифицировать, "
              f"я скажу об этом сразу."),
        ("p", "Если вы находитесь в Европейском союзе, к обработке в части, которая "
              "вас касается, применяется также GDPR, и перечисленные права "
              "предоставляются в объёме, который он устанавливает."),

        ("h2", "Утечки"),
        ("p", "Если произойдёт утечка, которая может вам навредить, я уведомлю "
              "надзорный орган в течение 72 часов с момента, когда о ней узнаю, "
              "и свяжусь с вами, если затронуты ваши данные."),

        ("h2", "Изменения"),
        ("p", "Если поменяется то, что собирается или сколько хранится, поменяется и "
              "этот текст, а дата редакции наверху сдвинется. Существенные изменения "
              "я не ввожу задним числом."),
    ],

    "en": [
        ("p", f"Version of {_C['updated']}. This site is operated by "
              f"<strong>{_who('en')}</strong>. For anything in this document, write to "
              f"<a href=\"mailto:{cfg.EMAIL}\">{cfg.EMAIL}</a>."),
        ("note", "In short: this site sets no cookies, loads no third-party trackers, "
                 "and holds no identifier that would recognise you on a later visit. "
                 "Personal data exists only once you submit the form yourself."),

        ("h2", "What is collected without your involvement"),
        ("p", "The site runs its own analytics. Its purpose is to show which articles "
              "get read to the end and where people leave — nothing beyond that."),
        ("ul", [
            "page address, language version and title;",
            "referrer and UTM tags, if you arrived through a tagged link;",
            "device type, operating system, browser and window size;",
            "clicks on links and buttons, scroll depth, attention time per section;",
            "steps taken in the project calculator.",
        ]),
        ("p", "Each event carries a <strong>session identifier</strong> — a random value "
              "held in your browser's <code>sessionStorage</code> that disappears with "
              "the tab. It links one visit into one chain and cannot recognise you "
              "later: your next visit gets a different one. There is no cross-session "
              "identifier, no cookie and no advertising pixel on this site."),
        ("p", "Your IP address is not stored in analytics."),

        ("h2", "What you send yourself"),
        ("p", "Through the contact form you provide a name, a way to reach you (email or "
              "Telegram) and the text of your enquiry. Stored alongside it: the page the "
              "form was sent from, the language, UTM tags and the session identifier, so "
              "that I know where the enquiry came from."),
        ("p", "Separately, an <strong>irreversible hash of your IP address</strong> is "
              "stored with a secret salt. It does exactly one job: limit how many "
              "submissions come from one source, so the form cannot be flooded. The IP "
              "cannot be recovered from it and it is used for nothing else."),
        ("p", "The legal basis is your consent, given by the checkbox under the form, "
              "and my legitimate interest in answering you. Consent can be withdrawn at "
              "any time by writing to the address above."),

        ("h2", "Where it is kept and who else sees it"),
        ("p", "Data is held in a Supabase database. The public key embedded in the page "
              "can only write analytics events and can read nothing at all. Form "
              "submissions are accepted by a separate server-side function; the public "
              "key cannot write them. Reading either one requires an authenticated "
              "user — that is, me."),
        ("p", "The processors that physically hold data: <strong>Supabase</strong> "
              "(storage), <strong>Resend</strong> (delivering the notification email) "
              "and <strong>GitHub Pages</strong> (serving the pages). Nobody else "
              "receives the data, and it is never sold."),
        ("p", "These services run outside Georgia, so processing involves an "
              "international transfer. It takes place on the basis of your consent and "
              "only to the extent needed to run the site and answer you."),

        ("h2", "How long it is kept"),
        ("table", {
            "caption": "Retention periods. Deletion is scheduled, not discretionary.",
            "head": ["What", "Period", "What happens then"],
            "rows": [
                ["Analytics events", "24 months", "Deleted by a scheduled job in the database"],
                ["Form submissions", "36 months", "Deleted by a scheduled job in the database"],
                ["IP hash", "with the submission", "Deleted in the same cycle"],
                ["Email and Telegram threads", "as long as the work needs them", "Deleted on your request"],
            ],
        }),

        ("h2", "Your rights"),
        ("p", "Under the Law of Georgia on Personal Data Protection you may:"),
        ("ul", [
            "find out whether your data is processed and receive a copy;",
            "have inaccurate data corrected;",
            "have data erased or processing stopped;",
            "withdraw consent, after which processing stops;",
            "lodge a complaint with the Georgian supervisory authority.",
        ]),
        ("p", f"To exercise any of these, write to "
              f"<a href=\"mailto:{cfg.EMAIL}\">{cfg.EMAIL}</a>. I answer within the "
              f"periods the law sets; if I need to identify you before answering, "
              f"I will say so straight away."),
        ("p", "If you are in the European Union, the GDPR also applies to the "
              "processing that concerns you, and the rights above are provided to the "
              "extent it requires."),

        ("h2", "Breaches"),
        ("p", "If a breach occurs that could harm you, I will notify the supervisory "
              "authority within 72 hours of becoming aware of it, and contact you if "
              "your data is affected."),

        ("h2", "Changes"),
        ("p", "If what is collected or how long it is kept changes, this text changes "
              "with it and the version date at the top moves. I do not introduce "
              "material changes retroactively."),
    ],
}
