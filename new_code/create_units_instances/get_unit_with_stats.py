from .classes.units import Unit


def get_unit_with_stats_from_data(data, unit_name):
    kwargs = {
        "attack": data.loc[unit_name, "Атака"],
        "defence": data.loc[unit_name, "Защита"],
        "min_damage": data.loc[unit_name, "Мин урон"],
        "max_damage": data.loc[unit_name, "Макс урон"],
        "health": data.loc[unit_name, "Здоровье"],
        "initiative": data.loc[unit_name, "Инициатива"],
        "speed": data.loc[unit_name, "Скорость"],
        "ammo": data.loc[unit_name, "Выстрелы"]
    }
    unit = Unit(unit_name, **kwargs)

    if data.loc[unit_name, "Большое"] == 1:
        unit.big = True
    else:
        unit.big = False

    return unit
