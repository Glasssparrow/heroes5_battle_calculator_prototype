import logging
from simulation_code.initiative.get_order_list import get_order_list, get_unit_types_for_order_list
from simulation_code.decisions.choose_tactic import choose_tactic
from simulation_code.decisions.choose_action import choose_action
from simulation_code.move.move import move
from simulation_code.visualisation.get_grid import get_grid
from simulation_code.melee_fight.melee import melee_fight


def can_act(unit):
    result = True
    if unit.morale_status < 0:
        return False
    for effect in unit.effects:
        if effect.cannot_act:
            result = False
    return result


def battle(unit1, unit2):

    unit1.color, unit2.color = "Красный", "Синий"

    logging.info(f"Настало время смертельной битвы между "
                 f"{unit1.quantity} {unit1.name} (цвет {unit1.color}) и "
                 f"{unit2.quantity} {unit2.name} (цвет {unit2.color})")

    choose_tactic(unit1, unit2)

    for x in range(100):

        order_list = get_order_list(unit1, unit2, list_len=7)
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

        logging.info(
            f"Наступает ход {active.quantity} шт. "
            f"(hp={active.soldier_hp}/{active.health}) "
            f"{active.name} (цвет {active.color})"
        )
        active.start_turn()

        if can_act(active):
            move_to, action, movement_type = choose_action(active, passive)

            if move_to[0] == active.position[0] and move_to[1] == active.position[1]:
                logging.info(
                    f"{active.name} (цвет {active.color}) решает стоять "
                    f"на месте и применить\"{action}\"")
            else:
                logging.info(
                    f"{active.name} (цвет {active.color}) решает передвинуться "
                    f"на {move_to[0]},{move_to[1]} и применить\"{action}\"")

            move(active, passive, move_to, movement_type)

            if action == "strike":
                move_to, action = melee_fight(active, passive)
                move(active=passive, passive=active,
                     move_to=move_to, movement_type="move_and_stay")
                # Выстрел если действие выстрел
        if active.morale_status != 0:
            active.initiative_position = 0.5

        active.end_turn()

        grid_after = get_grid(unit1, unit2)
        for row in range(10):
            logging.info(f"{grid_before[row]}     {grid_after[row]}")

        if unit2.hp == 0:
            logging.info(
                f"{unit1.name} (цвет {unit1.color}) побеждает!"
            )
            break
        elif unit1.hp == 0:
            logging.info(
                f"{unit2.name} (цвет {unit2.color}) побеждает!"
            )
            break
