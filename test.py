from code.read_data import get_units_tuple
from code.battle import battle


unit1, unit2 = get_units_tuple("Крестьянин", "Мечник", 10, 1)
battle(unit1, unit2)
