from pandas import read_excel
from .classes import Unit


def get_units_tuple(name1, name2, quantity1, quantity2):
    table = read_excel("database.xlsx", "Орден порядка")
    table.index = table["Существо"]
    table.pop("Существо")
    unit1 = Unit(
        name=name1,
        attack=table.loc[name1, "Атака"],
        defence=table.loc[name1, "Защита"],
        min_damage=table.loc[name1, "Мин урон"],
        max_damage=table.loc[name1, "Макс урон"],
        hp=table.loc[name1, "Здоровье"],
        initiative=table.loc[name1, "Инициатива"],
        speed=table.loc[name1, "Скорость"],
        quantity=quantity1
    )
    unit2 = Unit(
        name=name2,
        attack=table.loc[name2, "Атака"],
        defence=table.loc[name2, "Защита"],
        min_damage=table.loc[name2, "Мин урон"],
        max_damage=table.loc[name2, "Макс урон"],
        hp=table.loc[name2, "Здоровье"],
        initiative=table.loc[name2, "Инициатива"],
        speed=table.loc[name2, "Скорость"],
        quantity=quantity2
    )
    return unit1, unit2
