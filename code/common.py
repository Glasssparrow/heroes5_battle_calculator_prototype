from math import ceil


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        raise Exception("Число не >, не >, не = 0...")


def choose_first_strike(unit1, unit2):
    initiative_advantage_threshold = 1.2
    initiative_high_speed_threshold = 1.8
    speed_threshold = 7
    roll_coin_text = """Порядок хода будет решен монеткой."""
    minor_initiative_victory_text = """Первый ход получен за счет большей \
инициативы при равной скорости"""
    speed_victory_text = f"""Первый ход получен за счет большей \
скорости при большей, равной или незначительно меньшей инициативе. \
Чтобы инициатива могла перебить скорость нужно иметь преимущество \
минимум в {initiative_advantage_threshold} раз."""
    initiative_victory_text = f"""Первый ход получен за счет \
преимущества в инициативе более {initiative_advantage_threshold} раз."""
    speed_domination_text = """\
Первый ход получен благодаря значительной разнице в скорости. \
Второй юнит не может преодолеть необходимую дистанцию даже \
с дополнительными ходами от инициативы."""
    speed_threshold_text = f"""Первый ход получен благодаря тому \
что размеры карты не позволяют реализовать преимущество инициативы \
менее {initiative_high_speed_threshold} при скорости противника 
более {speed_threshold}."""
    speed_uncertainty_text = """Значительная разница как \
в инициативе так и в скорости. """

    fast_unit, slow_unit = unit2, unit1

    def victory(unit):
        unit.initiative_position = 0
        print(f"{unit.name} побеждает в борьбе за первый удар!")

    if unit1.speed == unit2.speed:
        if unit1.initiative > unit2.initiative:
            victory(unit1)
            print(minor_initiative_victory_text)
        elif unit1.initiative < unit2.initiative:
            victory(unit2)
            print(minor_initiative_victory_text)
        else:
            print(f"Инициатива и скорость равны. {roll_coin_text}")
    # Если не угадали меняем быстрый юнит.
    elif slow_unit.speed > fast_unit.speed:
        fast_unit, slow_unit = slow_unit, fast_unit
    elif slow_unit.initiative/fast_unit.initiative < 1.2:
        victory(fast_unit)
        print(speed_victory_text)
    elif fast_unit.speed < slow_unit.speed*2+1:
        victory(slow_unit)
        print(initiative_victory_text)
    elif (fast_unit.speed > speed_threshold and
            slow_unit.initiative/fast_unit.initiative <
            initiative_high_speed_threshold):
        victory(fast_unit)
        print(speed_threshold_text)
    elif (fast_unit.speed/slow_unit.speed >
            ceil(slow_unit.initiative/fast_unit.initiative)):
        victory(fast_unit)
        print(speed_domination_text)
    else:
        print(f"{speed_uncertainty_text} {roll_coin_text}")


