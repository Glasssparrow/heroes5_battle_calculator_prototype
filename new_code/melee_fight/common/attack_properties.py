from random import randint
from math import ceil


def get_attack_properties(unit):

    attack = unit.attack

    luck_modifier = unit.wheel_of_fate()
    multiplier = luck_modifier * unit.quantity
    min_damage = ceil(unit.min_damage * multiplier)
    max_damage = ceil(unit.max_damage * multiplier)
    damage = randint(min_damage, max_damage)

    return attack, damage
