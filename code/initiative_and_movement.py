from random import randint, random, uniform
from .common import sign
from math import ceil
from .battle.melee import fight
from .initiative.get_order_list import get_order_list
import logging


def your_turn(attacker, defender):
    fight(attacker, defender)


def battle(unit1, unit2):

    logging.info(f"Настало время смертельной битвы между "
                 f"{unit1.quantity} {unit1.name} и "
                 f"{unit2.quantity} {unit2.name}")

    for x in range(100):

        # Если существо выбили за 0 позицию на шкале, возвращаем в 0.
        for unit in [unit1, unit2]:
            if unit.initiative_position < 0:
                unit.initiative_position = 0

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
            attacker, defender = unit1, unit2
        elif unit2.initiative_position >= 1:
            attacker, defender = unit2, unit1
        # Если у обоих ниже 1 (может случиться из-за ошибки округления),
        # То спокойно объявляем что тот кто ближе достиг финиша.
        else:
            if unit1.initiative_position >= unit2.initiative_position:
                attacker, defender = unit1, unit2
            else:
                attacker, defender = unit2, unit1

        # Запускаем эффекты начала хода
        # Если юнит струсил, то хода никакого не будет, жмем ожидание
        attacker.start_turn()
        if "Трусость" in attacker.status_1_turn.keys():
            logging.info(f"{attacker.name} Трусит!")
            attacker.initiative_position = 0.5
        else:
            attacker.initiative_position = 0

            # Проводим ход атакующего
            your_turn(attacker, defender)
        # Запускаем эффекты конца хода
        attacker.end_turn()
        defender.timer(timer)

        endloop = False
        for winner, loser in [(unit1, unit2), (unit2, unit1)]:
            if loser.quantity == 0:
                logging.info(f"{loser.name} повержен. "
                             f"Осталось {winner.quantity} "
                             f"{winner.name}")
                endloop = True
        if endloop:
            break
