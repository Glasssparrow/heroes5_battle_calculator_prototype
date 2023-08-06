from random import randint
from math import ceil


def get_attack_properties(unit, fight_type):

    attack = unit.attack
    if fight_type == "melee":
        if unit.week_in_melee:
            range_modifier = 0.5
        else:
            range_modifier = 1
        if unit.chivalry_charge:
            chivalry_modifier = 1 + 0.05 * unit.moved
        else:
            chivalry_modifier = 1
    else:
        range_modifier = 1
        chivalry_modifier = 1
    luck_modifier = unit.wheel_of_fate()
    multiplier = (
        luck_modifier * unit.quantity * range_modifier * chivalry_modifier *
        unit.damage_multiplier
    )
    min_damage = ceil(unit.min_damage * multiplier)
    max_damage = ceil(unit.max_damage * multiplier)
    damage = randint(min_damage, max_damage)

    return attack, damage
