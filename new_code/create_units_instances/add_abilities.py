from new_code.create_units_instances.classes.skills import *

def add_unit_abilities_from_data(data, unit):
    abilities_list = data.loc[unit.name, "Способности"].split(",")
    for z in range(len(abilities_list)):
        abilities_list[z] = abilities_list[z].strip()

    # Иммунитеты
    for ability_name, word_from_data in {
        "blind_immune": "Иммунитет к слепоте",
        "berserk_immune": "Иммунитет к берсерку",
        "slow_immune": "Иммунитет к замедлению",
        "control_immune": "Иммунитет к контролю разума",
        "weakening_immune": "Иммунитет к ослаблению"
    }.items():
        if word_from_data in abilities_list:
            unit.__dict__[ability_name] = True
    if "Живое существо" in abilities_list:
        unit.__dict__["vampirism_immune"] = False

    # Боевые способности
    for ability_name, word_from_data in {
        "week_in_melee": "Штраф в ближнем бою",
        "melee_bash": "Оглушение",
        "shield": "Щит",
        "double_attack_if_kill": "Колун",
        "infinite_counterattack": "Бесконечный отпор",
        "counterattack_rage": "Боевое безумие",
        "dispell_strike": "Очищение",
        "chivalry_charge": "Рыцарский разбег",
        "vampire": "Вампиризм",
    }.items():
        if word_from_data in abilities_list:
            unit.__dict__[ability_name] = True

    # Способности для тестирования
    for ability_name, word_from_data in {
        "rage_of_the_dummy": "Гнев манекена",
    }.items():
        if word_from_data in abilities_list:
            unit.__dict__[ability_name] = True

    # Навыки
    for word_from_data, instance_of_skill in {
        "Оглушение": PeasantBash(),
    }.items():
        if word_from_data in abilities_list:
            unit.skills.append(instance_of_skill)
