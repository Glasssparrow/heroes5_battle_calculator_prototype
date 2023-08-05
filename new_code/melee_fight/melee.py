from .common.attack_properties import get_attack_properties


def strike(attacker, defender):
    attack, damage = get_attack_properties(attacker)
    defender.take_damage(attack, damage)


def melee_fight(attacker, defender):

    strike(attacker, defender)
