from simulation_code.main import test_battle
from get_data.read_database import read_database


data = read_database(["test_database"])

test_battle(
    data=data,
    unit1_name="Кошмар", unit2_name="Ополченец",
    number_of_battles=100, quantity_type="Количество",
    quantity1=100, quantity2=1000
)
