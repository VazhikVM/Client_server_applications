"""Unit-тесты сервера"""
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
import unittest
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from server import process_client_message


class TestServer(unittest.TestCase):

    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    ok_dict = {RESPONSE: 200}

    def test_ok_check(self):
        """
        Корректный запрос
        :return:
        """
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}),
                         self.ok_dict)

    def test_no_action(self):
        """
        Ошибка, если нет действия
        :return:
        """
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}},
        ), self.ok_dict)

    def teat_wrong_action(self):
        """
        Ошибка, если неизвестное действие
        :return:
        """
        self.assertEqual(process_client_message(
            {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}
        ), self.err_dict)

    def test_no_time(self):
        """
        Ошибка, если запрос не содержит штампа времени
        :return:
        """
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}
        ), self.err_dict)

    def test_no_user(self):
        """
        Ошибка - нет пользователя
        :return:
        """
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.1'}
        ), self.err_dict)

    def test_unknown_user(self):
        """
        Ошибка - не Guest
        :return:
        """
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest1'}}
        ), self.err_dict)


if __name__ == '__main__':
    unittest.main()
