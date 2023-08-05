

stats = ["attack", "attack_flat", "defence", "defence_flat",
         "min_damage", "min_damage_flat",
         "max_damage", "max_damage_flat",
         "initiative", "initiative_flat",
         "speed", "speed_flat",
         "luck", "luck_flat", "morale", "morale_flat"]


class Effect:

    def __init__(self):

        self.name = "default_name"

        self.timer = 0
        self.check_immune = []

        self.dispell_after_counterattack = False
        self.dispell_by_timer = False

        self.cannot_counterattack = False

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
        self.check_immune = ["machine"]

        self.dispell_after_counterattack = True
        self.cannot_counterattack = True
