"""3. Определить, какие из слов, поданных на вход программы, невозможно записать в байтовом типе. Для проверки
правильности работы кода используйте значения: «attribute», «класс», «функция», «type»"""

my_list = ['attribute', 'класс', 'type', 'функция']


def task_3(word):
    for i in word:
        try:
            i_bite = eval(f"b'{i}'")
            print(f"Байтовый тип слово '{i}' - {i_bite}, Тип - {type(i_bite)}, Длина - {len(i_bite)}", '-' * 10, sep='\n')
        except SyntaxError:
            print(f'Слово "{i}" невозможно записать в байтовом типе', '-' * 10, sep='\n')


task_3(my_list)