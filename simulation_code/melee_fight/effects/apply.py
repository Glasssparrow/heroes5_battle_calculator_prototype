from math import copysign
from simulation_code.move.distance import distance_between_units


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
