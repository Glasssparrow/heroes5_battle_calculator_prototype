from pandas import DataFrame
from .read_xls import read_xls
from simulation_code.test_time import test_time


@test_time
def read_database(databases_list):

    data = DataFrame()

    for file_name in databases_list:
        read_xls(file_name, data)

    return data
