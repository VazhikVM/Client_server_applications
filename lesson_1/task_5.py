"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
(предварительно определив кодировку выводимых сообщений)."""
import locale
import chardet
import subprocess
import platform

my_list = ['yandex.ru', 'youtube.com']


def task_5(word):
    default_encoding = locale.getpreferredencoding()
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    for i in word:
        args = ['ping', param, '1', i]
        result = subprocess.Popen(args, stdout=subprocess.PIPE)
        for j in result.stdout:
            result = chardet.detect(j)
            j = j.decode(result['encoding']).encode(default_encoding)
            print(j.decode(default_encoding))


task_5(my_list)
