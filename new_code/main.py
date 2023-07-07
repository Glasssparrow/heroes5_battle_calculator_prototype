from new_code.create_units_instances.get_data import get_data
from new_code.create_units_instances.get_unit_with_stats import get_unit_with_stats_from_data
from new_code.create_units_instances.get_unit_quantity import get_unit_quantity
from new_code.create_units_instances.add_abilities import add_unit_abilities_from_data
from new_code.battle.battle import battle
from code_of_the_program.test import test_time
import logging


@test_time
def test_battle(unit1_name, unit2_name, number_of_battles,
                quantity_type, quantity1, quantity2):

    # Читаем данные
    data = get_data()
    # Формируем экземпляры юнитов
    unit1 = get_unit_with_stats_from_data(data, unit1_name)
    unit2 = get_unit_with_stats_from_data(data, unit2_name)
    get_unit_quantity(quantity_type, quantity1, unit1, data)
    get_unit_quantity(quantity_type, quantity2, unit2, data)
    add_unit_abilities_from_data(data, unit1)
    add_unit_abilities_from_data(data, unit2)

    # Проверяем что цвета у юнитов разные
    if unit1.color == unit2.color:
        unit1.color = "Бесцветный"

    result = battle(unit1, unit2, number_of_battles)
