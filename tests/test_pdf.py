import pypdf
import os.path
from conftest import RESOURCES_PATH

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_number_of_pages():
    pdf_file_path = os.path.join(RESOURCES_PATH, 'docs-pytest-org-en-latest.pdf')
    with open(pdf_file_path, 'rb') as pdf_file:
        reader = pypdf.PdfReader(pdf_file)

        number_of_pages = len(reader.pages)

        expected_num_of_pages = 412

        assert number_of_pages == expected_num_of_pages


def test_first_page_text():
    pdf_file_path = os.path.join(RESOURCES_PATH, 'docs-pytest-org-en-latest.pdf')
    with open(pdf_file_path, 'rb') as pdf_file:
        reader = pypdf.PdfReader(pdf_file)

        first_page = reader.pages[0]

        text = first_page.extract_text()

        expected_first_page_text = (
            "pytest Documentation\nRelease 0.1\nholger krekel, trainer and consultant, "
            "https://merlinux.eu/\nJul 14, 2022"
        )

        assert text == expected_first_page_text


def test_number_of_images_on_first_page():
    pdf_file_path = os.path.join(RESOURCES_PATH, 'docs-pytest-org-en-latest.pdf')
    with open(pdf_file_path, 'rb') as pdf_file:
        reader = pypdf.PdfReader(pdf_file)
        first_page = reader.pages[0]
        count = 0
        image_path = ''
        for image_file in first_page.images:
            with open(
                os.path.join(RESOURCES_PATH, str(count) + image_file.name), 'wb'
            ) as fp:
                fp.write(image_file.data)
                image_path = os.path.join(
                    RESOURCES_PATH, str(count) + image_file.name
                )
                count += 1

    expected_number_of_images = 1

    assert count == expected_number_of_images

    os.remove(os.path.abspath(image_path))

