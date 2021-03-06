"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
«декоратор». Проверить кодировку созданного файла (исходить из того, что вам априори неизвестна кодировка этого файла!).
Затем открыть этот файл и вывести его содержимое на печать. ВАЖНО: файл должен быть открыт без ошибок вне зависимости
от того, в какой кодировке он был создан!"""
import locale

my_list = ['сетевое программирование', 'сокет', 'декоратор']

default_encoding = locale.getpreferredencoding()
with open('test_file.txt', 'w', encoding=default_encoding) as file:
    for i in my_list:
        file.write(f'{i}\n')
