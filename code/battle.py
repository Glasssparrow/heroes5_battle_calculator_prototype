from random import randint
from .common import choose_first_strike


def fight(attacker, defender):
    print(f"Ход {attacker.name}. Шкала инициативы: "
          f"{attacker.name}: {attacker.initiative_position}, "
          f"{defender.name}: {defender.initiative_position}")
    defender.take_damage(**attacker.return_attack_properties_dict())
    if defender.counterattack_token > 0 and defender.quantity > 0:
        attacker.take_damage(**defender.return_attack_properties_dict())
        defender.lose_counterattack_token()


def battle(unit1, unit2):

    print(f"Настало время смертельной битвы между "
          f"{unit1.quantity} {unit1.name} и "
          f"{unit2.quantity} {unit2.name}")

    def roll_coin():
        coin = randint(0, 1)
        if coin == 0:
            unit1.initiative_position += -0.001
        else:
            unit1.initiative_position += 0.001

    choose_first_strike(unit1, unit2)

    for x in range(100):
        if unit1.initiative_position == unit2.initiative_position:
            roll_coin()

        # Проверяем кто атакует
        attacker, defender = unit1, unit2
        if attacker.initiative_position > defender.initiative_position:
            attacker, defender = defender, attacker

        # Проводим ход атакующего
        attacker.start_turn()
        fight(attacker, defender)
        attacker.initiative_position += 1/attacker.initiative
        attacker.end_turn()

        if unit1.quantity == 0:
            print(f"{unit1.name} повержен. Осталось {unit2.quantity} "
                  f"{unit2.name}")
            break
        elif unit2.quantity == 0:
            print(f"{unit2.name} повержен. Осталось {unit1.quantity} "
                  f"{unit1.name}")
            break
