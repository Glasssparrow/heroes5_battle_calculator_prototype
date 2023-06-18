from random import choice, uniform


# Идея в том что нужно возвращать характеристику с учетом всех бафов и дебафов,
# а перезаписывать уже характеристику самого юнита.
class UnitStat:

    def __set_name__(self, owner, name):
        self.name = "_" + name
        self.stat = name
        self.flat_stat = name + "_flat"

    def __get__(self, instance, owner):
        result = instance.__dict__[self.name]
        for buff in instance.__dict__["effects"]:
            result += buff.__dict__[self.stat] * result
            result += buff.__dict__[self.flat_stat]

        if self.name in ["luck", "morale"]:
            if -5 <= result <= 5:
                return round(result, 0)
            elif result > 5:
                return 5
            else:
                return -5

        if result <= 0:
            result = 0
            if self.name == "initiative":
                result = 0.1

        if self.name == "min_damage":
            if result >= instance.max_damage:
                return instance.max_damage

        if self.name == "initiative":
            result = round(result, 1)
        else:
            result = round(result, 0)

        return result

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        instance.__dict__[self.name] = 0


class Unit:

    attack = UnitStat()
    defence = UnitStat()
    min_damage = UnitStat()
    max_damage = UnitStat()
    health = UnitStat()
    initiative = UnitStat()
    speed = UnitStat()
    luck = UnitStat()
    morale = UnitStat()

    # Предполагается что kwargs содержит только элементы из stats.
    # Остальные элементы словаря будут проигнорированы.
    def __init__(self, name, **kwargs):
        self.name = name
        self.initiative_position = uniform(0, 0.25)
        self.counterattack_token = 1
        self.color = choice(
            ["Красный", "Оранжевый", "Желтый", "Зеленый",
             "Голубой", "Синий", "Фиолетовый"]
        )
        self.effects = []

        stats = ["attack", "defence", "min_damage", "max_damage",
                 "health", "initiative", "speed",
                 "growth", "extra_growth", "ammo", "cost", "exp", "big"]
        for stat in stats:
            if stat not in kwargs.keys():
                raise ValueError(f"Не найден аргумент {stat}")
            self.__dict__[stat] = kwargs[stat]

        self.luck = 0
        self.morale = 0

    def apply_effect(self):
        pass
