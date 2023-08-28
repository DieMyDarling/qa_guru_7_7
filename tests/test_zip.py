import os.path
import zipfile

from conftest import RESOURCES_PATH


def test_zip():
    zip_file_path = os.path.join(RESOURCES_PATH, 'zip_file.zip')

    files = ['docs-pytest-org-en-latest.pdf',
             'file_example_XLS_10.xls',
             'file_example_XLSX_50.xlsx']

    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        for file in files:
            path_to_file = os.path.join(RESOURCES_PATH, file)

            zip_file.write(path_to_file, os.path.basename(path_to_file))

    file_names = zip_file.namelist()

    assert files == file_names

    os.remove(os.path.abspath(zip_file_path))
