import os.path

import xlrd

from conftest import RESOURCES_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_number_of_sheets():
    xls_file_path = os.path.join(RESOURCES_PATH, 'file_example_XLS_10.xls')
    book = xlrd.open_workbook(xls_file_path)
    expected_num_of_sheets = 1
    assert book.nsheets == expected_num_of_sheets


def test_names_of_sheets():
    xls_file_path = os.path.join(RESOURCES_PATH, 'file_example_XLS_10.xls')
    book = xlrd.open_workbook(xls_file_path)
    expected_sheet_name = ['Sheet1']
    assert book.sheet_names() == expected_sheet_name


def test_number_of_columns():
    xls_file_path = os.path.join(RESOURCES_PATH, 'file_example_XLS_10.xls')
    book = xlrd.open_workbook(xls_file_path)
    sheet = book.sheet_by_index(0)
    expected_num_of_cols = 8
    assert sheet.ncols == expected_num_of_cols


def test_number_of_rows():
    xls_file_path = os.path.join(RESOURCES_PATH, 'file_example_XLS_10.xls')
    book = xlrd.open_workbook(xls_file_path)
    sheet = book.sheet_by_index(0)
    expected_num_of_rows = 10
    assert sheet.nrows == expected_num_of_rows


def test_column_cross_row_cell_value():
    xls_file_path = os.path.join(RESOURCES_PATH, 'file_example_XLS_10.xls')
    book = xlrd.open_workbook(xls_file_path)
    sheet = book.sheet_by_index(0)
    row = 3
    col = 2
    expected_cell_value = 'Gent'
    assert sheet.cell_value(rowx=row, colx=col) == expected_cell_value


def test_value_of_rows():
    xls_file_path = os.path.join(RESOURCES_PATH, 'file_example_XLS_10.xls')
    book = xlrd.open_workbook(xls_file_path)
    expected_values = [
        [0.0, 'First Name', 'Last Name', 'Gender', 'Country', 'Age', 'Date', 'Id'],
        [1.0, 'Dulce', 'Abril', 'Female', 'United States', 32.0, '15/10/2017', 1562.0],
        [2.0,
         'Mara',
         'Hashimoto',
         'Female',
         'Great Britain',
         25.0,
         '16/08/2016',
         1582.0],
        [3.0, 'Philip', 'Gent', 'Male', 'France', 36.0, '21/05/2015', 2587.0],
        [4.0,
         'Kathleen',
         'Hanner',
         'Female',
         'United States',
         25.0,
         '15/10/2017',
         3549.0],
        [5.0,
            'Nereida',
            'Magwood',
            'Female',
            'United States',
            58.0,
            '16/08/2016',
            2468.0,
        ],
        [6.0, 'Gaston', 'Brumm', 'Male', 'United States', 24.0, '21/05/2015', 2554.0],
        [7.0, 'Etta', 'Hurn', 'Female', 'Great Britain', 56.0, '15/10/2017', 3598.0],
        [
            8.0,
            'Earlean',
            'Melgar',
            'Female',
            'United States',
            27.0,
            '16/08/2016',
            2456.0,
        ],
        [
            9.0,
            'Vincenza',
            'Weiland',
            'Female',
            'United States',
            40.0,
            '21/05/2015',
            6548.0,
        ],
    ]

    sheet = book.sheet_by_index(0)

    for i in range(sheet.nrows):
        assert sheet.row_values(i) == expected_values[i]
