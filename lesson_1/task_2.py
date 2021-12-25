"""2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это небходимо в автоматическом,
а не ручном режиме с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы
encode и decode) и определить тип, содержимое и длину соответствующих переменных."""

import subprocess


my_list = ['class', 'function', 'method']


def task_2(word):
    for i in word:
        print(f"Слово - '{i}', Тип - {type(i),} Длина - {len(i)}", sep='\n')
        i_bite = eval(f"b'{i}'")
        print(f"Байтовый тип слово '{i}' - {i_bite}, Тип - {type(i_bite)}, Длина - {len(i_bite)}", '-' * 10, sep='\n')


task_2(my_list)
