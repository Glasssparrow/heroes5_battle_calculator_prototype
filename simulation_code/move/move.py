from math import copysign


def move(active, passive, move_to, movement_type):
    if movement_type == "move_and_stay":
        active.moved = (
            copysign(active.position[0] - move_to[0], 1) +
            copysign(active.position[1] - move_to[1], 1)
        )
        active.position = move_to
    else:
        pass
    passive.moved = 0
