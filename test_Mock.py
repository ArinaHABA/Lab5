import unittest  # автоматизация тестов
import sys, os  # предоставляет системе особые параметры и функции
from unittest.mock import patch, Mock
# Когда функция оформлена через @patch, mock класса, метода или функции,
# переданная в качестве цели для @patch, возвращается и передается в качестве аргумента декорируемой функции.
import builder

sys.path.append(os.getcwd())  # добавить путь поиска модулей
from builder import *

class Burger_Test_Builder(unittest.TestCase):
    @patch.object(builder.Burger_Builder(), 'buns')
    # patch.object принимает объект и имя атрибута, который требуется исправить,
    # а также, при необходимости, значение для исправления.
    def test_buns(self, mock_buns):
        mock_buns.return_value = None
        self.assertEqual(Burger_Builder().buns(), None)