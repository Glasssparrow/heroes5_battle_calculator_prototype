from .common import sign
from math import ceil
from random import randint


class Unit:

    def __init__(self, name, quantity, attack, defence,
                 min_damage, max_damage, hp, initiative, speed,
                 ammo, cost, growth, extra_growth, exp, big,
                 **kwargs):
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
        self.ammo = ammo
        self.cost = cost
        self.growth = growth
        self.extra_growth = extra_growth
        self.exp = exp
        self.big = big
        self.abilities = kwargs
        self.initiative_position = 0.75
        self.counterattack_token = 1
        self.luck = 0
        self.morale = 0
        self.debuffs = {}
        self.buffs = {}
        self.status_1_turn = {}

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
        return amount_of_damage, quantity_before-self.quantity

    def return_attack_properties_dict(self):
        damage_dice = randint(0, self.max_damage - self.min_damage)
        luck_dice = randint(1, 10)
        damage = self.min_damage + damage_dice
        if self.luck > 0:
            if self.luck >= luck_dice:
                damage = damage*2
                print(f"Удача на стороне {self.name}")
        elif self.luck < 0:
            if abs(self.luck) >= luck_dice:
                damage = damage / 2
                print(f"Удача не на стороне {self.name}")

        return {
            "name": self.name,
            "quantity": self.quantity,
            "attack": self.attack,
            "damage": damage
        }

    def start_turn(self):
        # Выдаем новый жетон контратаки если старый использован
        self.counterattack_token = 1
        # Очищаем статусы на 1 ход
        self.status_1_turn = {}
        # Удаляем кончившиеся бафы.
        buffs_list = []
        for k, v in self.buffs.items():
            buffs_list.append(k)
        for x in buffs_list:
            if x in self.buffs.keys() and self.buffs[x] < 0:
                del self.buffs[x]
        # Удаляем кончившиеся дебафы.
        debuffs_list = []
        for k, v in self.debuffs.items():
            debuffs_list.append(k)
        for x in debuffs_list:
            if x in self.debuffs.keys() and self.debuffs[x] <= 0:
                del self.debuffs[x]
        # Проверяем не струсил ли юнит
        if self.morale < 0:
            dice = randint(1, 10)
            if abs(self.morale) >= dice:
                self.status_1_turn["Трусость"] = 1

    def end_turn(self):
        if self.morale > 0:
            dice = randint(1, 10)
            if self.morale >= dice:
                self.initiative_position = 0.5
                print(f"{self.name} Воодушевляется!")

    def lose_counterattack_token(self):
        # Теряем жетон только если нет особой способности
        if not self.abilities["infinite_counterattack"]:
            self.counterattack_token -= 1

    def timer(self, time):
        for k, v in self.debuffs.items():
            v -= time
        for k, v in self.buffs.items():
            v -= time

