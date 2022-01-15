"""Unit-тесты клиента"""
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
import unittest
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_presence, process_ans


class TestClient(unittest.TestCase):
    """
    Класс с тестами
    """

    def test_def_presense(self):
        """
        Тест корректного запроса
        """
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """
        Тест корректного запроса 200
        :return:
        """
        self.assertEqual(process_ans({RESPONSE: 200}))

    def test_400_ans(self):
        """
        Тест корректного разбора 400
        :return:
        """
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400: Bad Request')

    def test_no_response(self):
        """
        Тест исключения без поля RESPONSE
        :return:
        """
        self.assertEqual(ValueError, process_ans, {ERROR: 'Bad Request'})
