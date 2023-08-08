from math import copysign


def is_adjacent(unit1, unit2):
    if (copysign(unit1.position[0] - unit2.position[0], 1) < 2 or
       (copysign(unit1.position[1] - unit2.position[1], 1) < 2)):
        return True
    else:
        return False
