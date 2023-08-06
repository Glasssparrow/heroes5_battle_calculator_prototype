from simulation_code.create_units_instances.classes.skills import *


IMMUNITIES = {
    "blind_immune": "Иммунитет к слепоте",
    "berserk_immune": "Иммунитет к берсерку",
    "slow_immune": "Иммунитет к замедлению",
    "control_immune": "Иммунитет к контролю разума",
    "weakening_immune": "Иммунитет к ослаблению",
    "machine": "Механизм",
    "undead": "Нежить",
    "elemental": "Элементаль",
}

IMMUNITIES_REVERSE = {
    "vampirism_immune": "Живое существо"
}

BATTLE_ABILITIES = {
    "week_in_melee": "Штраф в ближнем бою",
    "melee_bash": "Оглушение",
    "shield": "Щит",
    "double_attack": "Двойной удар",
    "double_attack_if_kill": "Колун",
    "assault": "Штурм",
    "forbid_counterattack": "Враг не отвечает",
    "infinite_counterattack": "Бесконечный отпор",
    "dispell_strike": "Очищение",
    "chivalry_charge": "Рыцарский разбег",
    "vampire": "Вампиризм",
    "agility": "Ловкость",
    "blinding_strike": "Ослепляющий удар"
}

SKILLS = {
    "Оглушение": PeasantBash(),
    "Оглушение щитом": FootmanBash(),
    "Боевое безумие": BattleFrenzy(),
    "Ослепляющий удар": BlindingStrike(),
}

TESTING_ABILITIES = {

}

TESTING_SKILLS = {

}

