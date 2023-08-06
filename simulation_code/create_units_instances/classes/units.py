from random import choice, uniform, randint
from logging import info
from math import copysign, ceil
from simulation_code.constants import (
    IMMUNITIES, IMMUNITIES_REVERSE, BATTLE_ABILITIES, TESTING_ABILITIES
)


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

        if self.name in ["_luck", "_morale"]:
            if -5 <= result <= 5:
                return round(result, 0)
            elif result > 5:
                return 5
            else:
                return -5

        if result <= 0:
            result = 0
            if self.name == "_initiative":
                result = 0.1

        if self.name == "_min_damage" or self.name == "_max_damage":
            return instance.return_damage_into_range(result)

        if self.name in ["_initiative", "_damage_multiplier"]:
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
    initiative = UnitStat()
    speed = UnitStat()
    luck = UnitStat()
    morale = UnitStat()

    # ПЕРЕРАБОТАТЬ!!! (Да и в целом стоит привести дескрипторы в порядок)
    damage_multiplier = UnitStat()

    # Предполагается что kwargs содержит только элементы из stats.
    # Остальные элементы словаря будут проигнорированы.
    def __init__(self, name):
        self.name = name
        self.initiative_position = uniform(0, 0.25)
        self.counterattack_token = True
        self.color = choice(
            ["Красный", "Оранжевый", "Желтый", "Зеленый",
             "Голубой", "Синий", "Фиолетовый"]
        )
        self.effects = []
        self.skills = []

        self._attack = 1
        self._defence = 1
        self._min_damage = 1
        self._max_damage = 1
        self._initiative = 1
        self._speed = 1
        self._ammo = 1
        self._damage_multiplier = 1

        self._health = 1
        self.hp = 0
        self.max_hp = 0
        self.quantity = 0
        self._luck = 0
        self._morale = 0
        self.moved = 0

        # Иммунитеты
        for ability in IMMUNITIES.keys():
            self.__dict__[ability] = False

        for ability in IMMUNITIES_REVERSE.keys():
            self.__dict__[ability] = True

        # Боевые способности
        for ability in BATTLE_ABILITIES.keys():
            self.__dict__[ability] = False

        # Тестовые способности
        for ability in TESTING_ABILITIES.keys():
            self.__dict__[ability] = False

    def apply_effect(self, new_effect):
        effect_not_in_effects = True
        number_of_effect = 0
        for x in range(len(self.effects)):
            if self.effects[x].name == new_effect.name:
                effect_not_in_effects = False
                number_of_effect = x
        if effect_not_in_effects:
            info(f"На {self.name} (цвет {self.color}) "
                 f"наложен эффект {new_effect.name}")
            self.effects.append(new_effect)
        else:
            info(f"На {self.name} (цвет {self.color}) "
                 f"обновлен эффект {new_effect.name}")
            self.effects[number_of_effect].reapply(new_effect)

    def wheel_of_fate(self):
        if self.luck >= 0:
            dice = randint(0, 9)
            if self.luck > dice:
                info(f"Удача на стороне {self.name} (цвет {self.color})")
                return 2
            else:
                return 1
        else:
            dice = randint(0, 9)
            if self.luck > dice*(-1):
                info(f"Удача отворачивается от {self.name} (цвет {self.color})")
                return 0.5
            else:
                return 1

    def take_damage(self, attack, damage):
        amount_of_damage = round(
            damage *
            (1 + 0.05 * abs(attack - self.defence)) **
            copysign(1, attack - self.defence),
            0
        )
        soldier_hp_before = self.soldier_hp
        self.hp = self.hp - amount_of_damage
        quantity_before = self.quantity
        if self.hp < 0:
            self.hp = 0
        self.quantity = ceil(self.hp / self.health)
        info(
            f"{self.name} ({quantity_before} шт. "
            f"hp={soldier_hp_before}/{self.health}) "
            f"получает {amount_of_damage} "
            f"единиц урона. Погибло {quantity_before - self.quantity} "
            f"существ (hp={self.soldier_hp}/{self.health}).")
        return amount_of_damage, quantity_before - self.quantity

    def restore_hp(self, healing):
        quantity_before = self.quantity
        self.hp += healing
        hp_restored = healing
        if self.hp > self.max_hp:
            hp_restored -= self.hp - self.max_hp
            self.hp = self.max_hp
        self.quantity = ceil(self.hp/self.health)
        info(f"{self.name} (цвет {self.color}) восстанавливает {hp_restored} "
             f"здоровья. Возрождено {self.quantity-quantity_before} существ.")

    @property
    def soldier_hp(self):
        return int(self.hp - ((self.quantity-1) * self.health))

    @property
    def health(self):
        return int(self._health)

    @health.setter
    def health(self, value):
        self._health = value

    def return_damage_into_range(self, damage):
        if self._min_damage <= damage <= self._max_damage:
            return damage
        elif self._min_damage > damage:
            return self._min_damage
        else:
            return self._max_damage

    def lose_counterattack_token(self):
        if not self.infinite_counterattack:
            self.counterattack_token = False

    def lose_one_buff(self):
        buffs_numbers = []
        for i, effect in enumerate(self.effects):
            if effect.type == "buff" and effect.can_be_dispelled_by_enemy:
                buffs_numbers.append(i)
        if buffs_numbers:
            chosen_buff = choice(buffs_numbers)
            info(f"{self.name} (цвет {self.color}) теряет эффект "
                 f"{self.effects[chosen_buff].name}")
            del self.effects[chosen_buff]

    def start_turn(self):
        self.counterattack_token = True

        # Снимаем все эффекты спадающие в начале хода
        for_delete = []
        for i, effect in enumerate(self.effects):
            if effect.dispell_at_turn_start:
                for_delete.append(i)
        for_delete.sort(reverse=True)
        for x in for_delete:
            info(f"С {self.name} (цвет {self.color}) спадает эффект "
                 f"{self.effects[x].name}")
            del self.effects[x]
