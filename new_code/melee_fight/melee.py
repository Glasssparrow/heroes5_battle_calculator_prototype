from .common.attack_properties import get_attack_properties
from math import copysign


def strike(attacker, defender):
    attack, damage = get_attack_properties(attacker, "melee")
    defender.take_damage(attack, damage)


def melee_fight(attacker, defender):

    strike(attacker, defender)

    strike(defender, attacker)


def base_chance(attacker, defender):
    chance = (
            0.25 + copysign(1, attacker.hp - defender.hp) * 0.03 *
            (attacker.hp / defender.hp)
    )
    if chance < 0.05:
        chance = 0.05
    elif chance > 0.75:
        chance = 0.75
    return chance
