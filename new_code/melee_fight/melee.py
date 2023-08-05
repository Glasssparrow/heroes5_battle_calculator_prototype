from .common.attack_properties import get_attack_properties
from math import copysign
from new_code.move.distance import distance_between_units


def strike(attacker, defender):
    attack, damage = get_attack_properties(attacker, "melee")
    defender.take_damage(attack, damage)


def can_counter(attacker, target):
    can_attack = True
    for effect in attacker.effects:
        if effect.cannot_counterattack:
            return False
    return can_attack


def apply_effects_before_attack(attacker, target):
    chance = base_chance(attacker, target)
    for skill in attacker.skills:
        if skill.apply_before_attack:
            if skill.did_worked(
                chance, distance_between_units(attacker, target)
            ):
                enemy_have_immune = False
                for immune in skill.effect.immune_to_check():
                    if target.__dict__[immune]:
                        enemy_have_immune = True
                if skill.target == "self":
                    attacker.apply_effect(skill.effect)
                else:
                    target.apply_effect(skill.effect)


def melee_fight(attacker, defender):

    apply_effects_before_attack(attacker, defender)

    strike(attacker, defender)

    if can_counter(attacker=defender, target=attacker):
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
