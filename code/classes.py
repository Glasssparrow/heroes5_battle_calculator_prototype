from .common import sign
from math import ceil
from random import randint


class Unit:

    def __init__(self, name, attack, defence, min_damage,
                 max_damage, hp, quantity,
                 initiative, speed):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.soldier_hp = hp
        self.hp = hp * quantity
        self.quantity = quantity
        self.initiative = initiative
        self.speed = speed
        self.initiative_position = 0

    def take_damage(self, attack, damage, name, quantity):
        amount_of_damage = round(
            quantity * damage *
            (1 + 0.05 * abs(attack - self.defence)) **
            sign(attack - self.defence),
            0
        )
        self.hp = self.hp - amount_of_damage
        quantity_before = self.quantity
        if self.hp < 0:
            self.hp = 0
        self.quantity = ceil(self.hp/self.soldier_hp)
        print(f"{name} ({quantity} шт.) атакует {self.name} "
              f"({quantity_before} шт.) "
              f"и наносит {amount_of_damage} "
              f"единиц урона. Погибло {quantity_before-self.quantity} "
              f"существ.")

    def return_attack_properties_dict(self):
        dice = randint(0, self.max_damage - self.min_damage)
        damage = self.min_damage + dice
        return {
            "name": self.name,
            "quantity": self.quantity,
            "attack": self.attack,
            "damage": damage
        }
