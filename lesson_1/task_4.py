"""4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
байтовое и выполнить обратное преобразование (используя методы encode и decode)."""

my_list = ['разработка', 'администрирование', 'protocol', 'standard']


def task_4(word):
    for i in word:
        i_bite = str.encode(i, encoding='utf-8')
        print(i_bite)
        i_decode = bytes.decode(i_bite, encoding='utf-8')
        print(i_decode, '-' * 10, sep='\n')


task_4(my_list)
