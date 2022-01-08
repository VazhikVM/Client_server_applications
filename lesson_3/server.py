"""Программа-сервер"""
import json
import sys
import socket
from common.utils import send_message, get_message
from common.variables import ACTION, PRESENCE, DEFAULT_PORT, MAX_CONNECTIONS, TIME, USER,\
    ACCOUNT_NAME, RESPONSE, RESPONDEFAULT_IP_ADDRESSE, ERROR


def process_client_message(message):
    """
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клиента, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message
    :return:
    """
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONDEFAULT_IP_ADDRESSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    """
    Загрузка параметров командной строки, если нет параметров,
    то задаем значения по умолчанию
    server.py -p 8888 -a 127.0.0.1
    :return:
    """
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print('В качестве порта может быть указано только число в диапозоне'
              'от 1024 до 65535')
        sys.exit(1)
    # Затем загружаем какой адрес слушать

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
    except IndexError:
        print('После параметра \'a\'-необходимо указать адрес, '
              'который будет слушать')
        sys.exit(1)

    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
