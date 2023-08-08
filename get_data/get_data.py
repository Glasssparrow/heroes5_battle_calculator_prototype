from pandas import read_excel
from pandas import DataFrame


def read_table(file, sheet, index):
    tmp = read_excel(file, sheet)
    tmp.index = tmp[index]
    tmp.pop(index)
    return tmp


def get_data():
    meta = read_table("database.xlsx", "Метаданные", "Название листа")
    data_dict = {}
    for table_list in meta.index:
        data_dict[table_list] = read_table("database.xlsx",
                                           table_list, "Существо")
    table = DataFrame()
    for sheet_name, datasheet in data_dict.items():
        for row in datasheet.index:
            for column in datasheet.columns:
                table.loc[row, column] = datasheet.loc[row, column]
            for column in meta.columns:
                table.loc[row, column] = meta.loc[sheet_name, column]

    return table