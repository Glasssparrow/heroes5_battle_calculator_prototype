from .common.attack_properties import get_attack_properties
from .effects.apply import apply_effects_before_attack
from .effects.dispell import dispell_after_counterattack


def strike(attacker, defender):
    attack, damage = get_attack_properties(attacker, "melee")
    defender.take_damage(attack, damage)


def can_counter(attacker, target):
    can_attack = True
    if not attacker.counterattack_token:
        return False
    for effect in attacker.effects:
        if effect.cannot_counterattack:
            return False
    return can_attack


def melee_fight(attacker, defender):

    apply_effects_before_attack(attacker, defender)

    strike(attacker, defender)

    if can_counter(attacker=defender, target=attacker):
        strike(defender, attacker)
        defender.lose_counterattack_token()

    dispell_after_counterattack(defender)
