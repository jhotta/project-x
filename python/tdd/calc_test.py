import unittest
from calculator import Calculator


class TddInPythonExample(unittest.TestCase):

    calc = Calculator()

    def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2, 2)
        self.assertEqual(4, result)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')

    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)

    def test_calculator_returns_error_message_if_x_arg_not_number_2(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
