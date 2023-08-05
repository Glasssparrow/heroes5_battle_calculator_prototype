from new_code.constants import (
    IMMUNITIES, IMMUNITIES_REVERSE, BATTLE_ABILITIES, SKILLS,
    TESTING_ABILITIES, TESTING_SKILLS
)


def add_unit_abilities_from_data(data, unit):
    abilities_list = data.loc[unit.name, "Способности"].split(",")
    for z in range(len(abilities_list)):
        abilities_list[z] = abilities_list[z].strip()

    # Иммунитеты
    for ability_name, word_from_data in IMMUNITIES.items():
        if word_from_data in abilities_list:
            unit.__dict__[ability_name] = True
    for ability_name, word_from_data in IMMUNITIES_REVERSE.items():
        if word_from_data in abilities_list:
            unit.__dict__[ability_name] = False

    # Боевые способности
    for ability_name, word_from_data in BATTLE_ABILITIES.items():
        if word_from_data in abilities_list:
            unit.__dict__[ability_name] = True

    # Навыки
    for word_from_data, instance_of_skill in SKILLS.items():
        if word_from_data in abilities_list:
            unit.skills.append(instance_of_skill)

    # Способности для тестирования
    for ability_name, word_from_data in TESTING_ABILITIES.items():
        if word_from_data in abilities_list:
            unit.__dict__[ability_name] = True

    # Тестовые навыки
    for word_from_data, instance_of_skill in TESTING_SKILLS.items():
        if word_from_data in abilities_list:
            unit.skills.append(instance_of_skill)
