from .effects import *
from random import random


class Skill:

    def __init__(self):
        self.effect = None
        self.skill_range = 100
        self.apply_before_attack = False
        self.apply_after_counterattack = False
        self.check_immune = []
        self.target = "self"

    @staticmethod
    def did_worked(base_chance=1, skill_range=100):
        return True

    def return_effect(self):
        return self.effect


class PeasantBash(Skill):

    def __init__(self):
        super().__init__()
        self.effect = Bash()
        self.apply_before_attack = True
        self.target = "enemy"

    def did_worked(self, base_chance=1, skill_range=100):
        dice = random()
        if dice < base_chance:
            return True
        else:
            return False


class FootmanBash(PeasantBash):

    def did_worked(self, base_chance=1, skill_range=100):
        dice = random()
        chance = 1 - (1 - base_chance) ** 1.5
        if dice < base_chance:
            return True
        else:
            return False


class BattleFrenzy(Skill):

    def __init__(self):
        super().__init__()
        self.effect = CounterattackDamageMultiplier()
        self.apply_after_counterattack = True


class BlindingStrike(Skill):

    def __init__(self):
        super().__init__()
        self.effect = Blind()
        self.apply_before_attack = True
        self.target = "enemy"

    def did_worked(self, base_chance=1, skill_range=100):
        dice = random()
        if dice < base_chance:
            return True
        else:
            return False


class CounterattackBlocker(Skill):

    def __init__(self):
        super().__init__()
        self.effect = BlockCounterattack()
        self.apply_before_attack = True
        self.target = "enemy"

    def did_worked(self, base_chance=1, skill_range=100):
        dice = random()
        if dice < base_chance:
            return True
        else:
            return False
