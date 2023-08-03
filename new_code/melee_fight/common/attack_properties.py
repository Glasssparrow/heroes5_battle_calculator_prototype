from random import randint
from math import ceil


def get_attack_properties(unit):

    attack = unit.attack

    min_damage = unit.min_damage
    max_damage = unit.max_damage
    multiplier = unit.wheel_of_fate()
    damage = randint(ceil(min_damage*multiplier), ceil(max_damage*multiplier))

    return attack, damage
