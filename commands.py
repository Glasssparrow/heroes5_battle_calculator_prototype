

def get_factions(data):
    factions_list = []
    for index in data.index:
        if data.loc[index, "Фракция"] not in factions_list:
            factions_list.append(data.loc[index, "Фракция"])
    factions = ""
    for element in factions_list:
        factions = f"{factions}, {element}"
    return factions_list


def stats_of_unit(data, unit_name):
    if unit_name not in data.index:
        result = "Что-то пошло не так =\\"
    else:
        result = (
            f'Атака={data.loc[unit_name, "Атака"]}, '
            f'Защита={data.loc[unit_name, "Защита"]}, '
            f'Мин урон={data.loc[unit_name, "Мин урон"]}, '
            f'Макс урон={data.loc[unit_name, "Макс урон"]}, '
            f'Здоровье={data.loc[unit_name, "Здоровье"]}, '
            f'Инициатива={data.loc[unit_name, "Инициатива"]},'
            f'Скорость={data.loc[unit_name, "Скорость"]}, \n'
            f'Выстрелы={data.loc[unit_name, "Выстрелы"]}, '
            f'Мана={data.loc[unit_name, "Мана"]}, '
            f'Цена={data.loc[unit_name, "Цена"]}, '
            f'Опыт={data.loc[unit_name, "Опыт"]}, \n'
            f'Прирост={data.loc[unit_name, "Прирост"]}, '
            f'Прирост+={data.loc[unit_name, "Прирост+"]}, \n'
            f'Способности={data.loc[unit_name, "Способности"]}, \n'
            f'Большое={data.loc[unit_name, "Большое"]}, '
            f'Уровень={data.loc[unit_name, "Уровень"]}, '
            f'Улучшение={data.loc[unit_name, "Улучшение"]}, '
            f'Фракция={data.loc[unit_name, "Фракция"]} '
        )
    return result
