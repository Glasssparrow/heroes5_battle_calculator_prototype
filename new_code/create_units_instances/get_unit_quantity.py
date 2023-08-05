from math import floor


def get_unit_quantity(quantity_type, quantity, unit, data):
    if quantity_type == "Количество" or quantity_type == 0:
        unit.quantity = quantity
    elif quantity_type == "Золото" or quantity_type == 1:
        unit.quantity = floor(quantity / data.loc[unit.name, "Цена"])
    elif quantity_type == "Прирост" or quantity_type == 2:
        unit.quantity = (
            data.loc[unit.name, "Прирост"]
        ) * quantity
    elif quantity_type == "Прирост+" or quantity_type == 3:
        unit.quantity = (
            data.loc[unit.name, "Прирост"] + data.loc[unit.name, "Прирост+"]
        ) * quantity
    else:
        unit.quantity = 1

    unit.hp = unit.quantity * unit.health
    unit.max_hp = unit.hp
