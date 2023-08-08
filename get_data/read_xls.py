from pandas import read_excel
from pandas import DataFrame
from .constants import *


def read_table(file, sheet, index):
    tmp = read_excel(file, sheet)
    tmp.index = tmp[index]
    tmp.pop(index)
    return tmp


def read_xls(database_name, data=None):
    path = f"database/{database_name}.xlsx"
    meta = read_table(path, METADATA_SHEET_NAME, METADATA_COLUMN_NAME)
    if data is None:
        data = DataFrame()
    elif not isinstance(data, DataFrame):
        data = DataFrame()
    data_dict = {}
    for table_list in meta.index:
        data_dict[table_list] = read_table(path,
                                           table_list, SHEET_INDEX)
    for sheet_name, datasheet in data_dict.items():
        for row in datasheet.index:
            for column in datasheet.columns:
                data.loc[row, column] = datasheet.loc[row, column]
            for column in meta.columns:
                data.loc[row, column] = meta.loc[sheet_name, column]

    return data
