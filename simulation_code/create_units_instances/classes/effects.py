

stats = ["attack", "attack_flat",
         "defence", "defence_flat",
         "min_damage", "min_damage_flat",
         "max_damage", "max_damage_flat",
         "speed", "speed_flat",
         "luck", "morale",
         "initiative", "damage_multiplier", ]


class Effect:

    def __init__(self):

        self.name = "default_name"

        self.timer = 0
        self.type = "buff"
        self.check_immune = []
        self.can_be_dispelled_by_enemy = False

        self.dispell_at_turn_start = False
        self.dispell_after_counterattack = False
        self.dispell_by_attack = False
        self.dispell_by_timer = False

        self.cannot_counterattack = False
        self.cannot_act = False
        self.fear = False

        self.bash = False

        for stat in stats:
            self.__dict__[stat] = 0

    def reapply(self, new_instance):
        self.timer = new_instance.timer

    def immune_to_check(self):
        return self.check_immune


class Bash(Effect):

    def __init__(self):
        super().__init__()
        self.name = "bash"
        self.buff = "debuff"
        self.check_immune = ["machine"]
        self.bash = True

        self.dispell_after_counterattack = True
        self.cannot_counterattack = True


class CounterattackDamageMultiplier(Effect):

    def __init__(self):
        super().__init__()
        self.name = "battle_frenzy"
        self.damage_multiplier = 0.5
        self.can_be_dispelled_by_enemy = True

        self.dispell_at_turn_start = True

    def reapply(self, new_instance):
        self.damage_multiplier = (
            self.damage_multiplier * 1.5 + 0.5
        )


class Agility(Effect):

    def __init__(self, moved):
        super().__init__()
        self.name = "agility"
        self.defence_flat = moved * 2
        self.can_be_dispelled_by_enemy = True
        self.dispell_at_turn_start = False


class BlockCounterattack(Effect):

    def __init__(self):
        super().__init__()
        self.name = "block_counterattack"
        self.buff = "debuff"
        self.check_immune = []

        self.dispell_after_counterattack = True
        self.cannot_counterattack = True


class Blind(Effect):

    def __init__(self):
        super().__init__()
        self.name = "blind"
        self.buff = "debuff"
        self.check_immune = ["undead", "elemental", "machine"]

        self.timer = 10
        self.cannot_act = True
        self.cannot_counterattack = True

        self.dispell_by_timer = True
        self.dispell_by_attack = True


class Fear(Effect):

    def __init__(self):
        super().__init__()
        self.name = "fear"
        self.buff = "debuff"
        self.dispell_after_counterattack = True
        self.cannot_counterattack = True
        self.check_immune = ["control_immune"]
        self.fear = False
