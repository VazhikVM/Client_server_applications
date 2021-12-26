"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в
файле YAML-формата. Для этого:

Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с
помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml


def write_yaml(dict_data, way_file):
    with open(way_file, 'w', encoding='utf-8') as file_yaml:
        yaml.dump(dict_data, file_yaml, allow_unicode=True)


if __name__ == '__main__':
    my_dict = {('a', 'b', 'c'): ['a', 'b', 'c'], 5: 5, '€_3': {'€_1': '€_1', '€_2': '€_2'}}
    write_yaml(my_dict, 'file_yaml.yaml')

    with open('file_yaml.yaml', 'r', encoding='utf-8') as file:
        file_read = yaml.full_load(file)
        print(file_read)
