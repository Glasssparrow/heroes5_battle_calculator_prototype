from code.read_data.read_data import get_data
from code.read_data.get_unit_tuple import get_units_tuple
from code.initiative_and_movement import battle
from code.test import test_time
import logging


@test_time
def test():
    data = get_data()

    for x in range(100):
        if x < 100:
            logging.basicConfig(level=logging.INFO,
                                filename=f"log/battle{x}.log",
                                filemode="w", force=True)
        else:
            logging.basicConfig(level=logging.INFO,
                                filename=f"log/battle100+.log",
                                filemode="w", force=True)
        unit1, unit2 = get_units_tuple("Крестьянин", "Боевой грифон", 20, 1,
                                       data)

        unit1.color = "Красный"
        unit2.color = "Синий"
        unit1.initiative = 500
        unit1.morale = 0
        unit1.luck = 0
        battle(unit1, unit2)


test()
