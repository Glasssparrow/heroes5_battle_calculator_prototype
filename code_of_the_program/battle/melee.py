from random import randint, random, uniform
from code_of_the_program.common import sign
from math import ceil
import logging


def strike(attacker, defender, counterattack=False):
    # Характеристики атакующего
    attacker_stats = attacker.return_attack_properties_dict()
    # Если есть штраф за ближний бой
    if attacker.abilities["week_in_melee"]:
        attacker_stats["damage"] = 0.5 * attacker_stats["damage"]

    if counterattack:
        # Если есть боевое безумие, то умножаем на него урон.
        attacker_stats["damage"] *= (
            attacker.status_1_turn.get("counterattack_rage", 1))
        # Теряем жетончик контратаки (исключение - бесконечный отпор)
        attacker.lose_counterattack_token()
        # Увеличиваем модификатор боевого безумия если оно есть.
        if attacker.abilities["counterattack_rage"]:
            attacker.status_1_turn["counterattack_rage"] = (
                1.5 * attacker.status_1_turn.get("counterattack_rage", 1)
            )

    # Бьём
    damage, kills = defender.take_damage(
        **attacker_stats)

    if attacker.abilities["vampire"] and defender.abilities["alive"]:
        attacker.hp += damage*0.5
        quantity_before_healing = attacker.quantity
        attacker.quantity = ceil(attacker.hp/attacker.soldier_hp)
        logging.info(f"{attacker.name} восстанавливает {damage*0.5} "
                     f"здоровья. Возродилось "
                     f"{attacker.quantity-quantity_before_healing}"
                     f"существо")

    return kills


def did_it_worked(attacker, defender):
    bash_was_activated = False
    if (
            attacker.abilities["melee_bash"]
            and defender.hp != 0
            and not defender.abilities["device"]
    ):
        bash_dice = random()
        bash_chance = (0.25 + sign(attacker.hp - defender.hp) * 0.03 *
                       (attacker.hp / defender.hp))
        if bash_chance < 0.05:
            bash_chance = 0.05
        elif bash_chance > 0.75:
            bash_chance = 0.75
        if bash_chance >= bash_dice:
            bash_was_activated = True
    return bash_was_activated


def fight(attacker, defender):
    first_attack_kills = strike(attacker=attacker, defender=defender)
    # Проверяем сработало ли оглушение
    bash = False
    if attacker.abilities["melee_bash"] and defender.hp != 0:
        bash = did_it_worked(attacker, defender)
    if bash:
        defender.initiative_position -= 0.5
        logging.info(f"{attacker.name} оглушает противника!")


    # Проводим ответную атаку если есть жетон, юнит жив и не оглушен.
    if (
        defender.counterattack_token > 0 and
        defender.hp != 0 and
        not bash
    ):
        kills = strike(attacker=defender, defender=attacker,
                       counterattack=True)


    # Проводим вторую атаку если есть Колун или Двойной удар
    # Вторая атака не может оглушить т.к.
    # нет юнита с двойным оглушающим ударом
    if (attacker.abilities["double_attack_if_kill"] and
            first_attack_kills >= 1 or
            attacker.abilities["double_attack"]):
        kills = strike(attacker=attacker, defender=defender)
        # Проверяем сработало ли оглушение
        second_bash = False
        if attacker.abilities["melee_bash"] and defender.hp != 0:
            second_bash = did_it_worked(attacker, defender)
        if second_bash:
            defender.initiative_position -= 0.5
            logging.info(f"{attacker.name} оглушает противника!")
        # Проводим ответную атаку если есть жетон, юнит жив и не оглушен.
        # 2 контрудар только при условии 2 атаки
        if (
                defender.counterattack_token > 0 and
                defender.hp != 0 and
                not second_bash
        ):
            kills = strike(attacker=defender, defender=attacker,
                           counterattack=True)