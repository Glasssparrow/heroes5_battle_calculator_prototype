from random import choice, uniform


class Unit:

    def __init__(self, name, attack, defence,
                 min_damage, max_damage, hp, initiative, speed,
                 ammo, cost, growth, extra_growth, exp, big,
                 **kwargs):
        self.name = name
        self._attack = attack
        self._defence = defence
        self._min_damage = min_damage
        self._max_damage = max_damage
        self._soldier_hp = hp
        self._initiative = initiative
        self._speed = speed
        self._ammo = ammo
        self._cost = cost
        self._growth = growth
        self._extra_growth = extra_growth
        self._exp = exp
        self._big = big
        self._big = False
        self.initiative_position = uniform(0, 0.25)
        self.counterattack_token = 1
        self.color = choice(
            ["Красный", "Оранжевый", "Желтый", "Зеленый",
             "Голубой", "Синий", "Фиолетовый"]
        )
