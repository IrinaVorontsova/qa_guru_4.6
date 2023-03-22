import zipfile

import PyPDF2 as PyPDF2


# Написать автотест, запаковывающий в zip-архив несколько разных файлов – pdf, xlsx, csv,
# – и кладущий его в папку resources.
# Реализовать чтение и проверку в ассертах содержимого каждого файла из архива, не распаковывая его.


def add_to_zip(file_path, file_name):

    with zipfile.ZipFile('//resources//myzip', 'w') as myzip:
        myzip.write(file_path, file_name)

def file_pdf_compare(file_orig, file_zip):
    add_to_zip("test_files//pdf_test.pdf", "pdf_test")
    with zipfile.ZipFile('//resources//myzip', 'r') as zip_file:
        with zip_file.open(file_zip, 'r') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            assert len(pdf_reader.pages) == 10, "PDF file should have 10 pages."


def test_files():
    # with zipfile.ZipFile('resources/test.zip') as zip_:
    #     print(zip_.namelist())

    # with zipfile.ZipFile('//resources//test.zip', 'w') as myzip:
    #     myzip.write("test_files//pdf_test.pdf", "pdf_test")
    #
    # with zipfile.ZipFile('//resources//myzip', 'r') as zip_file:
    #     with zip_file.open("pdf_test", 'r') as pdf_file:
    #         pdf_reader = PyPDF2.PdfReader(pdf_file)
    #         assert len(pdf_reader.pages) == 10, "PDF file should have 10 pages."
    files_to_zip = ['pdf_test.pdf', 'xlsx_test.xlsx', 'cvs_test.csv']

    # создание архива
    with zipfile.ZipFile('resources/files.zip', 'w') as zip_file:
        for file in files_to_zip:
            zip_file.write(file)


def test_read_pdf():
    with zipfile.ZipFile('//resources//myzip', 'r') as zip_file:
        with zip_file.open('file1.pdf', 'r') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            assert len(pdf_reader.pages) == 10, "PDF file should have 10 pages."


def test_read_csv():
    with zipfile.ZipFile('//resources//myzip', 'r') as zip_file:
        with zip_file.open('file3.csv', 'r') as csv_file:
            count_row = 0
            for _ in csv_file:
                count_row += 1
            assert 7 == count_row


# def test_read_xlsx():
#     with zipfile.ZipFile('//resources//myzip', 'r') as zip_file:
#         with zip_file.open('file2.xlsx', 'r') as xlsx_file:
#             book = openpyxl.load_workbook(xlsx_file)
#             sheet = book.active
#             assert 'First Name' in sheet['B1'].value
#             assert 'Dulce' in sheet['B2'].value
#
#
#             ```python
#             import zipfile
#
#             # список файлов для архивирования
#             files_to_zip = ['file1.pdf', 'file2.xlsx', 'file3.csv']
#
#             # создание архива
#             with zipfile.ZipFile('resources/files.zip', 'w') as zip_file:
#                 for file in files_to_zip:
#                     zip_file.write(file)
#
#             import zipfile
#
#             # открытие архива
#             with zipfile.ZipFile('resources/files.zip', 'r') as zip_file:
#                 # чтение содержимого файлов
#                 pdf_content = zip_file.read('file1.pdf')
#                 xlsx_content = zip_file.read('file2.xlsx')
#                 csv_content = zip_file.read('file3.csv')
#
#             # проверка содержимого файлов
#             assert b'%PDF-' in pdf_content  # проверка, что файл pdf является pdf-документом
#             assert b'xlsx' in xlsx_content  # проверка, что файл xlsx содержит строку 'xlsx'
#             assert b',' in csv_content  # проверка, что файл csv содержит символ ','
#             ```