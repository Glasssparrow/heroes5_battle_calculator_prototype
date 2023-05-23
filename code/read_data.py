from pandas import read_excel
from .classes import Unit


def get_units_tuple(name1, name2, quantity1, quantity2):
    table = read_excel("database.xlsx", "Орден порядка")
    table.index = table["Существо"]
    table.pop("Существо")
    dictionary = {}
    for init_name, unit_quantity in {name1: quantity1,
                                     name2: quantity2}.items():
        if table.loc[init_name, "Большое"] == 0:
            big = False
        else:
            big = True
        abilities_list = table.loc[init_name, "Способности"].split(",")
        for z in range(len(abilities_list)):
            abilities_list[z] = abilities_list[z].strip()
        abilities_dict = {}
        for k, v in {
            "alive": "Живое существо",
            "undead": "Нежить",

            "taxpayer": "Налогоплательщик",

            "week_in_melee": "Штраф в ближнем бою",
            "close_range_shot": "Точный выстрел",
            "accuracy": "Стрельба без штрафа",
            "double_shot": "Двойной выстрел",
            "piercing_shot": "Пробивающий выстрел",

            "bash": "Оглушение",
            "strong_bash": "Сильное оглушение",
            "charge": "Рыцарский разбег",
            "double_attack_if_kill": "Колун",
            "double_attack": "Двойной удар",
            "vampire": "Вампиризм",

            "shield": "Щит",

            "infinite_counterattack": "Бесконечный отпор",
            "counterattack_rage": "Боевое безумие",

            "blind_immune": "Иммунитет к слепоте",
            "berserk_immune": "Иммунитет к берсерку"
        }.items():
            if v in abilities_list:
                abilities_dict[k] = True
            else:
                abilities_dict[k] = False
        dictionary[init_name] = Unit(
            name=init_name,
            quantity=unit_quantity,
            attack=table.loc[init_name, "Атака"],
            defence=table.loc[init_name, "Защита"],
            min_damage=table.loc[init_name, "Мин урон"],
            max_damage=table.loc[init_name, "Макс урон"],
            hp=table.loc[init_name, "Здоровье"],
            initiative=table.loc[init_name, "Инициатива"],
            speed=table.loc[init_name, "Скорость"],
            ammo=table.loc[init_name, "Выстрелы"],
            cost=table.loc[init_name, "Цена"],
            exp=table.loc[init_name, "Опыт"],
            growth=table.loc[init_name, "Прирост"],
            extra_growth=table.loc[init_name, "Прирост+"],
            big=big,
            **abilities_dict
        )
    return dictionary[name1], dictionary[name2]
