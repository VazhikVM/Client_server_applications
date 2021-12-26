"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в
него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
import csv
import re
from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()


def get_data(list_file):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for file in list_file:
        with open(file, 'rb') as f:
            for line in f:
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
        coding_file = detector.result['encoding']

        with open(file, 'r', encoding=coding_file) as f:
            for row in f:
                item = re.sub(r'\n', '', row)
                item = re.split(':', item)
                if item[0] == 'Изготовитель системы':
                    os_prod_list.append(re.sub("^\s+|\s+$", '', item[1]))
                elif item[0] == 'Название ОС':
                    os_name_list.append(re.sub("^\s+|\s+$", '', item[1]))
                elif item[0] == 'Код продукта':
                    os_code_list.append(re.sub("^\s+|\s+$", '', item[1]))
                elif item[0] == 'Тип системы':
                    os_type_list.append(re.sub("^\s+|\s+$", '', item[1]))

    for i in range(len(os_prod_list)):
        main_data.append([
            os_prod_list[i],
            os_name_list[i],
            os_code_list[i],
            os_type_list[i],
        ])

    return main_data


def write_to_csv(file_puth_csv, date):
    list_data = get_data(date)
    with open(file_puth_csv, 'w', encoding='utf-8') as csv_file:
        f_write = csv.writer(csv_file)
        for row in list_data:
            f_write.writerow(row)


if __name__ == "__main__":
    files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    write_to_csv('csv.csv', files)

    with open('csv.csv') as f:
        print(f.read())
