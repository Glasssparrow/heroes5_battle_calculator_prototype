from .common.attack_properties import get_attack_properties
from .effects.apply import (
    apply_effects_before_attack, base_chance, apply_effects_after_counterattack,
)
from .effects.dispell import dispell_after_counterattack
from random import random
from logging import info
from math import ceil


def strike(attacker, defender):
    attack, damage = get_attack_properties(attacker, "melee")
    damage_taken, soldiers_died = defender.take_damage(attack, damage)
    if attacker.dispell_strike:
        defender.lose_one_buff()
    if attacker.vampire:
        attacker.restore_hp(ceil(damage_taken/2))
    return damage_taken, soldiers_died


def can_counter(attacker, target):
    can_attack = True
    if target.forbid_counterattack:
        return False
    if not attacker.counterattack_token:
        return False
    for effect in attacker.effects:
        if effect.cannot_counterattack:
            return False
    return can_attack


def melee_fight(attacker, defender):

    apply_effects_before_attack(attacker, defender)

    damage1, kills1 = strike(attacker, defender)

    if can_counter(attacker=defender, target=attacker):
        info(f"{defender.name} (цвет {defender.color}) контратакует.")
        strike(defender, attacker)
        defender.lose_counterattack_token()
        apply_effects_after_counterattack(attacker=defender, target=attacker)

    dispell_after_counterattack(defender)

    if (
        attacker.double_attack or
        attacker.double_attack_if_kill and kills1 > 0 or
        attacker.assault and base_chance(attacker, defender) > random()
    ):
        info(f"{attacker.name} (цвет {attacker.color}) атакует повторно.")
        damage2, kills2 = strike(attacker, defender)

        if can_counter(attacker=defender, target=attacker):
            info(f"{defender.name} (цвет {defender.color}) контратакует.")
            strike(defender, attacker)
            defender.lose_counterattack_token()
            apply_effects_after_counterattack(attacker=defender, target=attacker)

        dispell_after_counterattack(defender)
