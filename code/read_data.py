from pandas import read_excel
from .classes import Unit
from pandas import DataFrame


def read_table(file, sheet, index):
    tmp = read_excel(file, sheet)
    tmp.index = tmp[index]
    tmp.pop(index)
    return tmp


def get_units_tuple(name1, name2, quantity1, quantity2):
    meta = read_table("database.xlsx", "Метаданные", "Название листа")
    data_dict = {}
    for table_list in meta.index:
        data_dict[table_list] = read_table("database.xlsx",
                                           table_list, "Существо")
    table = DataFrame()
    for sheet_name, datasheet in data_dict.items():
        for row in datasheet.index:
            for column in datasheet.columns:
                table.loc[row, column] = datasheet.loc[row, column]
            for column in meta.columns:
                table.loc[row, column] = meta.loc[sheet_name, column]

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
            "device": "Механизм",
            "elemental": "Элементаль",

            "taxpayer": "Налогоплательщик",  # Крестьяне
            "always_first_strike": "Всегда бьет первым",  # Пригодится

            "close_range_shot": "Точный выстрел",  # Арбалетчик
            "accuracy": "Стрельба без штрафа",
            "double_shot": "Двойной выстрел",  # Эльфы лучники
            "piercing_shot": "Пробивающий выстрел",  # Синие эльфы лучники
            "range_bash": "Оглушающий выстрел",  # Эльфы лучники
            "counterattack_shot": "Ответный выстрел",
            "week_in_range": "Штраф в дальнем бою",

            "shield": "Щит",  # Латники
            "acid_blood": "Кислотная кровь",  # гидры

            "ghost": "Бестелесность",
            "scary_look": "Смертельный взгляд",  # Призрачный дракон
            "bravery": "Храбрость",  # Минотавры
            "poison": "Отравление",  # Ассасины
            "regeneration": "Регенерация",  # Гидры

            "melee_bash": "Оглушение",
            "chivalry_charge": "Рыцарский разбег",
            "charge": "Удар с разбега",  # ящеры
            "double_attack_if_kill": "Колун",  # Ревнители веры
            "double_attack": "Двойной удар",  # Минотавры
            "vampire": "Вампиризм",
            "week_in_melee": "Штраф в ближнем бою",
            "no_counter": "Враг не отвечает",
            "blinding_strike": "Ослепляющий удар",
            "intimidation": "Атака страхом",  # Кони
            "extra_kill": "Гарантированное убийство",  # Пещерные
            "damage_for_quantity": "Убойный клинок",  # Пещерные
            "weakening_strike": "Ослабляющий удар",  # зомби
            "curse_strike": "Наложение проклятия",  # Призрачный дракон
            "sorrow_strike": "Удар скорби",  # Астральный дракон

            "fear_aura": "Аура страха",  # Кони,
            "fire_aura": "Иссушающая аура",  # Кони
            "poisoning_aura": "Отравляющая аура",  # зомби

            "infinite_counterattack": "Бесконечный отпор",
            "counterattack_rage": "Боевое безумие",  # Боевые грифоны

            "blind_immune": "Иммунитет к слепоте",
            "berserk_immune": "Иммунитет к берсерку",
            "slow_immune": "Иммунитет к замедлению",
            "control_immune": "Иммунитет к контролю разума",
            "weakening_immune": "Иммунитет к ослаблению"
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
