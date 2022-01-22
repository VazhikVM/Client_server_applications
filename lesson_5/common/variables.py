"""Канстанты"""
import logging

# Порт по умолчанию для сетевого взаимодействия
DEFAULT_PORT = 7777
# IP адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONNECTIONS = 5
# Максимальня длина сообщений в байтах
MAX_PACKAGE_LENGTH = 1028
# Кодировка проекта
ENCODING = 'utf-8'

# Протокол JIM основный ключи
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
RESPONDEFAULT_IP_ADDRESSE = 'respondefault_ip_addressse'

# Текущий уровень логирования
LOGGING_LEVEL = logging.DEBUG

