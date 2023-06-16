from code_of_the_program.read_data.read_data import get_data
from code_of_the_program.read_data.get_unit_tuple import get_units_tuple
from code_of_the_program.initiative_and_movement import battle
from code_of_the_program.test import test_time
import logging


@test_time
def test():
    data = get_data()

    for x in range(10):
        if x < 100:
            logging.basicConfig(level=logging.INFO,
                                filename=f"log/battle{x}.log",
                                filemode="w", force=True)
        else:
            logging.basicConfig(level=logging.INFO,
                                filename=f"log/battle100+.log",
                                filemode="w", force=True)
        unit1, unit2 = get_units_tuple("Крестьянин", "Ополченец",
                                       20, 20,
                                       data)

        unit1.color = "Красный"
        unit2.color = "Синий"
        # unit1.initiative = 500
        unit1.morale = 0
        unit1.luck = 0
        battle(unit1, unit2)


test()
