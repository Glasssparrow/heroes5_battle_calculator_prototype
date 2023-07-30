import logging
from new_code.initiative.get_order_list import get_order_list


def battle(unit1, unit2):

    # choose_tactics(unit1, unit2)

    for x in range(100):

        # Если существо выбили за 0 позицию на шкале, возвращаем в 0.
        for unit in [unit1, unit2]:
            if unit.initiative_position < 0:
                unit.initiative_position = 0

        order_list = get_order_list(unit1, unit2)
