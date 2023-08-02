import logging
from new_code.initiative.get_order_list import get_order_list, get_unit_types_for_order_list
from new_code.decisions.choose_tactic import choose_tactic
from new_code.decisions.choose_action import choose_action
from new_code.move.move import move
from new_code.visualisation.get_grid import get_grid
from new_code.melee_fight.melee import melee_fight


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

        grid_before = get_grid(unit1, unit2)

        if unit1.initiative_position == 0:
            active, passive = unit1, unit2
        else:
            active, passive = unit2, unit1

        move_to, action = choose_action(active, passive)

        if move_to[0] == active.position[0] and move_to[1] == active.position[1]:
            logging.info(
                f"{active.name} (цвет {active.color}) решает стоять "
                f"на месте и применить\"{action}\"")
        else:
            logging.info(
                f"{active.name} (цвет {active.color}) решает передвинуться "
                f"на {move_to[0]},{move_to[1]} и применить\"{action}\"")

        move(active, passive, move_to)

        if action == "strike":
            melee_fight(active, passive)

        if action == "strike":
            melee_fight(active, passive)

        grid_after = get_grid(unit1, unit2)
        for row in range(10):
            logging.info(f"{grid_before[row]}     {grid_after[row]}")
