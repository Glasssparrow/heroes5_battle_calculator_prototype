import logging
from new_code.initiative.get_order_list import get_order_list, get_unit_types_for_order_list


def battle(unit1, unit2):

    # choose_tactics(unit1, unit2)

    for x in range(100):

        order_list = get_order_list(unit1, unit2)
        if unit1.name == unit2.name:
            logging.info(order_list)
        order_with_types = get_unit_types_for_order_list(order_list, unit1, unit2)
        logging.info(order_with_types)
