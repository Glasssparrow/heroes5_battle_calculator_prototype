from math import ceil
from random import randint


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        raise Exception("Число не >, не >, не = 0...")
