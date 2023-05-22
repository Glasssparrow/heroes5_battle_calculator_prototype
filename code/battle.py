from random import randint


def fight(attacker, defender):
    defender.take_damage(**attacker.return_attack_properties_dict())


def battle(unit1, unit2):

    print(f"Настало время смертельной битвы между "
          f"{unit1.quantity} {unit1.name} и "
          f"{unit2.quantity} {unit2.name}")

    def roll_coin(unit):
        coin = randint(0, 1)
        if coin == 0:
            unit.initiative_position += -0.01
        else:
            unit.initiative_position += 0.01

    def attack_first(unit):
        unit.initiative_position += -0.02

    if unit1.speed == unit2.speed:
        if unit1.initiative > unit2.initiative:
            attack_first(unit1)
            print(f"{unit1.name} получает первый ход "
                  f"за счет большей инициативы.")
        elif unit1.initiative < unit2.initiative:
            attack_first(unit2)
            print(f"{unit2.name} получает первый ход "
                  f"за счет большей инициативы.")
        else:
            print(f"Существа обладают равной скоростью и инициативой. "
                  f"Право первого хода будет разыграно монеткой")
    elif unit1.speed > unit2.speed:
        if (unit2.initiative > unit1.initiative * 2 and
                unit1.speed < unit2.initiative/unit1.initiative*unit2.speed):
            attack_first(unit2)
            print(f"{unit2.name} получает первый ход "
                  f"за счет подавляющего преимущества в инициативе.")
        else:
            attack_first(unit1)
            print(f"{unit1.name} получает первый ход "
                  f"за счет большей скорости.")
    elif unit1.speed < unit2.speed:
        if (unit1.initiative > unit2.initiative * 2 and
                unit2.speed < unit1.initiative/unit2.initiative*unit1.speed):
            attack_first(unit1)
            print(f"{unit1.name} получает первый ход "
                  f"за счет подавляющего преимущества в инициативе.")
        else:
            attack_first(unit2)
            print(f"{unit2.name} получает первый ход "
                  f"за счет большей скорости.")

    for x in range(100):
        if unit1.initiative_position == unit2.initiative_position:
            roll_coin(unit1)
        if unit1.initiative_position < unit2.initiative_position:
            fight(unit1, unit2)
            if unit2.quantity != 0: fight(unit2, unit1)
            unit1.initiative_position += 1/unit1.initiative
        else:
            fight(unit2, unit1)
            if unit1.quantity != 0: fight(unit1, unit2)
            unit1.initiative_position += 1 / unit1.initiative
        if unit1.quantity == 0:
            print(f"{unit1.name} повержен. Осталось {unit2.quantity} "
                  f"{unit2.name}")
            break
        elif unit2.quantity == 0:
            print(f"{unit2.name} повержен. Осталось {unit1.quantity} "
                  f"{unit1.name}")
            break
