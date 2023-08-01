from random import randint
import logging


def choose_tactic(unit1, unit2):

    # Выдаём юнитам случайное расположение.
    unit1.position = (randint(0, 9), randint(0, 1), )
    unit2.position = (randint(0, 9), randint(10, 11), )

    unit1.tactic = "berserk"
    logging.info(f"{unit1.name} (цвет {unit1.color}) решает действовать бездумно!")
    unit2.tactic = "dummy"
    logging.info(f"{unit2.name} (цвет {unit2.color}) стоять и ничего не делать!")
