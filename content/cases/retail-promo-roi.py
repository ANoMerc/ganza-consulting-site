# -*- coding: utf-8 -*-
CASE = dict(
    order=1,
    accent="yellow",
    client={"en": "Clothing retail chain · 25 stores · Eastern Europe",
            "ru": "Сеть магазинов одежды · 25 точек · Восточная Европа"},
    stat={"en": "+22% promo ROI", "ru": "+22% ROI акций"},
    title={"en": "Which promotions actually pay", "ru": "Какие акции действительно окупаются"},
    problem={
        "en": "Margin was falling despite constant promotions. Several promo types, "
              "twenty-five stores, plenty of traffic and revenue data — and no one able to "
              "say which promotion did the work and which just moved the discount around.",
        "ru": "Прибыль падала, несмотря на постоянные акции. Несколько типов промо, "
              "двадцать пять магазинов, много данных по трафику и выручке — и никто не мог "
              "сказать, какая акция сработала, а какая просто переложила скидку.",
    },
    did={
        "en": "Pulled everything into one table: traffic before, during and after each "
              "promotion, sales for the same three windows, floor area, store format, city, "
              "promo code, promo type and dates. Then a live test — one new promotion "
              "design against three the chain already ran, plus a control — and a proposal "
              "to pair discounts with an event on the street rather than a discount alone.",
        "ru": "Свёл всё в одну таблицу: трафик до, во время и после каждой акции, продажи "
              "за те же три окна, площадь магазина, формат, город, код акции, тип и даты. "
              "Дальше живой тест — один новый вариант акции против трёх, которые сеть уже "
              "проводила, плюс контроль — и предложение сочетать скидку с событием на "
              "улице, а не просто скидку.",
    },
    result={"en": "+22% return on promotions against the chain's own previous promo results",
            "ru": "+22% к отдаче от акций по сравнению с прошлыми акциями самой сети"},
    honest={
        "en": "The comparison was against previous promotions, not against a held-back "
              "group of stores — the control was between promo types, not between shops. "
              "That is the weaker of the two designs and I would insist on a store-level "
              "control group next time: some of the +22% belongs to seasonality and I "
              "cannot separate it out. I also expected a larger effect than this one.",
        "ru": "Сравнение шло с прошлыми акциями, а не с отложенной группой магазинов — "
              "контроль был между типами акций, а не между точками. Это более слабая "
              "схема, и в следующий раз я бы настаивал на контрольной группе магазинов: "
              "часть из этих 22% принадлежит сезонности, и отделить её я не могу. Честно "
              "говоря, я ожидал результата лучше.",
    },
    read=dict(slug="audit-nobody-reads", ru="Почему отчёты не меняют бизнес", en="Why reports don't change anything"),
    tags=["Analytics", "Retail", "Pricing"],
)
