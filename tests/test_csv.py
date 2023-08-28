import csv
import os

from conftest import RESOURCES_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_csv_file_data():
    csv_file_path = os.path.join(RESOURCES_PATH, 'new_csv.csv')
    with open(csv_file_path, 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    data = []

    with open(csv_file_path) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        for row in csvreader:
            data.append(row)

    expected_value_row1 = ['Bonny', 'Born', 'Peter']
    expected_value_row2 = ['Alex', 'Serj', 'Yana']

    assert data[0] == expected_value_row1
    assert data[1] == expected_value_row2

    os.remove(os.path.abspath(csv_file_path))

