from random import randint, random, uniform
from .common import sign
from math import ceil
from .battle.melee import fight
from .initiative.get_order_list import get_order_list
from code_of_the_program.decisionmaker.distance_and_visualisation import *
from code_of_the_program.decisionmaker.decisionmaker import decision_maker, choose_tactics
import logging


def use_action(active, passive, action):
    if action == "wait":
        pass
    elif action == "melee_attack":
        fight(attacker=active, defender=passive)


def battle(unit1, unit2):

    logging.info(f"Настало время смертельной битвы между "
                 f"{unit1.quantity} {unit1.name} и "
                 f"{unit2.quantity} {unit2.name}")

    unit1.position, unit2.position = get_random_positions()
    choose_tactics(unit1, unit2)

    for x in range(100):

        # Если существо выбили за 0 позицию на шкале, возвращаем в 0.
        for unit in [unit1, unit2]:
            if unit.initiative_position < 0:
                unit.initiative_position = 0

        order_list = get_order_list(unit1, unit2)

        # Находим время за которое один из юнитов достигнет 1.
        time_need_1 = (1 - unit1.initiative_position) / unit1.initiative
        time_need_2 = (1 - unit2.initiative_position) / unit2.initiative
        time = min(time_need_2, time_need_1)
        # Продвигаем юниты на шкале инициативы
        unit1.initiative_position += time * unit1.initiative
        unit2.initiative_position += time * unit2.initiative
        timer = time * 10

        logging.info(f"Шкала инициативы: "
                     f"{unit1.name}: {unit1.initiative_position}, "
                     f"{unit2.name}: {unit2.initiative_position}")

        # Устанавливаем в атакующую позицию того у кого позиция 1
        if unit1.initiative_position >= 1:
            active, passive = unit1, unit2
        elif unit2.initiative_position >= 1:
            active, passive = unit2, unit1
        # Если у обоих ниже 1 (может случиться из-за ошибки округления),
        # То спокойно объявляем что тот кто ближе достиг финиша.
        else:
            if unit1.initiative_position >= unit2.initiative_position:
                active, passive = unit1, unit2
            else:
                active, passive = unit2, unit1

        logging.info(get_visualisation(unit1.position, unit2.position))

        # Запускаем эффекты начала хода
        # Если юнит струсил, то хода никакого не будет, жмем ожидание
        active.start_turn()
        if "Трусость" in active.status_1_turn.keys():
            logging.info(f"{active.name} Трусит!")
            active.initiative_position = 0.5
        else:
            active.initiative_position = 0

            command = decision_maker(active, passive)

            active.position += command.move

            logging.info(get_visualisation(unit1.position, unit2.position))

            # Проводим ход активного юнита
            use_action(active, passive, command.action)
        # Запускаем эффекты конца хода
        active.end_turn()
        passive.timer(timer)

        endloop = False
        for winner, loser in [(unit1, unit2), (unit2, unit1)]:
            if loser.quantity == 0:
                logging.info(f"{loser.name} повержен. "
                             f"Осталось {winner.quantity} "
                             f"{winner.name}")
                endloop = True
        if endloop:
            break
