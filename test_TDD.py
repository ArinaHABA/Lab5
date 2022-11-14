import unittest  # автоматизация тестов
import sys, os  # предоставляет системе особые параметры и функции

from builder import *  # импорт из builder

sys.path.append(os.getcwd())  # добавить путь поиска модулей

class Burger_Test_Builder(unittest.TestCase):
    builder = Burger_Builder()

    def test_hamburger_builder(self):
        self.assertEqual(Director.Hamburger(self), None)

    def test_cheeseburger_builder(self):
        self.assertEqual(Director.Cheeseburger(self), None)