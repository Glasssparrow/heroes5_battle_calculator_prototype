from math import copysign


def distance_between_units(unit1, unit2):
    distance = (
        copysign(unit1.position[0] - unit2.position[0], 1) +
        copysign(unit1.position[1] - unit2.position[1], 1)
    )
    return distance
