from code.read_data import get_units_tuple
from code.battle import battle


unit1, unit2 = get_units_tuple("Крестьянин", "Ангел", 100, 1)
unit1.initiative = 50
battle(unit1, unit2)
