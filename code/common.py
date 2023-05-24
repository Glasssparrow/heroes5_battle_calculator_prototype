from math import ceil
from random import randint


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        raise Exception("Число не >, не >, не = 0...")


def choose_first_strike(unit1, unit2):

    def victory(unit):
        unit.initiative_position = 0.9999
        print(f"{unit.name} побеждает в борьбе за первый удар! "
              f"Рейтинги (скорость*инициатива) {rate1}:{rate2}")

    rate1 = unit1.initiative*unit1.speed
    rate2 = unit2.initiative*unit2.speed

    if rate1 > rate2:
        victory(unit1)
    elif rate1 < rate2:
        victory(unit2)
    else:
        if randint(0, 1) == 0:
            victory(unit1)
        else:
            victory(unit2)




