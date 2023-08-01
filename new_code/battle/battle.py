import logging
from new_code.initiative.get_order_list import get_order_list, get_unit_types_for_order_list
from new_code.decisions.choose_tactic import choose_tactic


def battle(unit1, unit2):
    logging.info(f"Настало время смертельной битвы между "
                 f"{unit1.quantity} {unit1.name} (цвет {unit1.color}) и "
                 f"{unit2.quantity} {unit2.name} (цвет {unit2.color})")

    choose_tactic(unit1, unit2)

    # choose_tactics(unit1, unit2)

    for x in range(100):

        order_list = get_order_list(unit1, unit2)
        order_with_types = get_unit_types_for_order_list(order_list, unit1, unit2)
        if unit1.name == unit2.name:
            logging.info(order_list)
        else:
            logging.info(order_with_types)
