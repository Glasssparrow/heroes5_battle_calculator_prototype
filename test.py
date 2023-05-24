from code.read_data import get_units_tuple
from code.battle import battle
from code.test import test_time


@test_time
def test():
    unit1, unit2 = get_units_tuple("Крестьянин", "Боевой грифон", 20, 1)
    unit1.initiative = 50
    unit1.morale = 0
    unit1.luck = 0
    battle(unit1, unit2)


test()
