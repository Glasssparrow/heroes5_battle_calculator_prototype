from .classes.units import Unit


def get_unit_with_stats_from_data(data, unit_name):
    unit = Unit(unit_name)

    unit.attack = data.loc[unit_name, "Атака"]
    unit.defence = data.loc[unit_name, "Защита"]
    unit.min_damage = data.loc[unit_name, "Мин урон"]
    unit.max_damage = data.loc[unit_name, "Макс урон"]
    unit.health = data.loc[unit_name, "Здоровье"]
    unit.initiative = data.loc[unit_name, "Инициатива"]
    unit.speed = data.loc[unit_name, "Скорость"]
    unit.ammo = data.loc[unit_name, "Выстрелы"]

    if data.loc[unit_name, "Большое"] == 1:
        unit.big = True
    else:
        unit.big = False

    return unit
