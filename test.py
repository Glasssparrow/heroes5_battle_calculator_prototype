from simulation_code.main import test_battle
from get_data.read_database import read_database
from constants import ALL_DATABASES


data = read_database(ALL_DATABASES)

result = test_battle(
    data=data,
    unit1_name="Крестьянин", unit2_name="Крестьянин",
    number_of_battles=1000, quantity_type="Количество",
    quantity1=100, quantity2=100
)

print(result)
