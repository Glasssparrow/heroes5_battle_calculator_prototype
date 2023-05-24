from random import randint, random, uniform
from .common import choose_first_strike, sign
from math import ceil


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
        print(f"{attacker.name} восстанавливает {damage*0.5} "
              f"здоровья. Возродилось "
              f"{attacker.quantity-quantity_before_healing}"
              f"существо")

    return kills


def use_bash(attacker, defender):
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
        bash = use_bash(attacker, defender)
    if bash:
        defender.initiative_position -= 0.5
        print(f"{attacker.name} оглушает противника!")


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
            second_bash = use_bash(attacker, defender)
        if second_bash:
            defender.initiative_position -= 0.5
            print(f"{attacker.name} оглушает противника!")
        # Проводим ответную атаку если есть жетон, юнит жив и не оглушен.
        # 2 контрудар только при условии 2 атаки
        if (
                defender.counterattack_token > 0 and
                defender.hp != 0 and
                not second_bash
        ):
            kills = strike(attacker=defender, defender=attacker,
                           counterattack=True)


def your_turn(attacker, defender):
    fight(attacker, defender)


def battle(unit1, unit2):

    print(f"Настало время смертельной битвы между "
          f"{unit1.quantity} {unit1.name} и "
          f"{unit2.quantity} {unit2.name}")

    choose_first_strike(unit1, unit2)

    for x in range(100):

        # Если существо выбили за 0 позицию на шкале, возвращаем в 0.
        for unit in [unit1, unit2]:
            if unit.initiative_position < 0:
                unit.initiative_position = 0

        # Находим время за которое один из юнитов достигнет 1.
        time_need_1 = (1 - unit1.initiative_position) / unit1.initiative
        time_need_2 = (1 - unit2.initiative_position) / unit2.initiative
        time = min(time_need_2, time_need_1)
        # Продвигаем юниты на шкале инициативы
        unit1.initiative_position += time * unit1.initiative
        unit2.initiative_position += time * unit2.initiative
        timer = time * 10

        print(f"Шкала инициативы: "
              f"{unit1.name}: {unit1.initiative_position}, "
              f"{unit2.name}: {unit2.initiative_position}")

        # Устанавливаем в атакующую позицию того у кого позиция 1
        if unit1.initiative_position >= 1:
            attacker, defender = unit1, unit2
        elif unit2.initiative_position >= 1:
            attacker, defender = unit2, unit1
        # Если у обоих ниже 1 (может случиться из-за ошибки округления),
        # То спокойно объявляем что тот кто ближе достиг финиша.
        else:
            if unit1.initiative_position >= unit2.initiative_position:
                attacker, defender = unit1, unit2
            else:
                attacker, defender = unit2, unit1

        # Запускаем эффекты начала хода
        # Если юнит струсил, то хода никакого не будет, жмем ожидание
        attacker.start_turn()
        if "Трусость" in attacker.status_1_turn.keys():
            print(f"{attacker.name} Трусит!")
            attacker.initiative_position = 0.5
        else:
            attacker.initiative_position = 0

            # Проводим ход атакующего
            your_turn(attacker, defender)
        # Запускаем эффекты конца хода
        attacker.end_turn()
        defender.timer(timer)

        endloop = False
        for winner, loser in [(unit1, unit2), (unit2, unit1)]:
            if loser.quantity == 0:
                print(f"{loser.name} повержен. Осталось {winner.quantity} "
                      f"{winner.name}")
                endloop = True
        if endloop:
            break
