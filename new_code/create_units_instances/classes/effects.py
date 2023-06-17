from random import choice


class Effect:

    def __init__(self, name, timer=100, until_new_turn=False,
                 dispel_after_hit=False, cannot_act=False, **kwargs):
        self.name = name

        self.timer = timer
        self.until_new_turn = until_new_turn
        self.dispel_after_hit = dispel_after_hit

        self.cannot_act = cannot_act

        self.stats = ["attack", "attack_flat", "defence", "defence_flat",
                      "min_damage", "min_damage_flat",
                      "max_damage", "max_damage_flat",
                      "health", "health_flat", "initiative", "initiative_flat",
                      "speed", "speed_flat",
                      "luck", "luck_flat", "morale", "morale_flat"]
        for stat in kwargs.keys():
            if stat not in self.stats:
                raise ValueError(f"{stat} не является характеристикой.")
        for stat in self.stats:
            if stat in kwargs.keys():
                self.__dict__[stat] = kwargs[stat]
            else:
                self.__dict__[stat] = 0

    def reapply(self, new_instance):
        for stat in self.stats:
            self.__dict__[stat] = new_instance.__dict__[stat]
        self.timer = new_instance.timer
