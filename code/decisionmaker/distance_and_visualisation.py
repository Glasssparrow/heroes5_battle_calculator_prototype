from random import randint
from math import ceil


def get_random_positions():
    dice1 = randint(4, 8)
    dice2 = randint(4, 8)
    distance = dice1 + dice2
    position1 = ceil((21 - distance) / 2)
    position2 = position1 + distance
    return position1, position2


def get_visualisation(position1, position2):
    visualisation = ""
    for x in range(21):
        if x == position1-1:
            visualisation += "0"
        elif x == position2-1:
            visualisation += "1"
        else:
            visualisation += "."
    return visualisation
