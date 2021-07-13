
import unittest
from lambda_function import Calculator


class Test_Calculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_calculator_class(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition_function(self):
        result = self.calculator.addition(2, 3)
        expected = 5
        self.assertEqual(result, expected)

    def test_sub_function(self):
        result = self.calculator.sub(10, 6)
        expected = 4
        self.assertEqual(result, expected)

    def test_divide_function(self):
        result = self.calculator.divide(10, 2)
        expected = 5
        self.assertEqual(result, expected)

    def test_multiply_function(self):
        result = self.calculator.multiply(10, 2)
        expected = 20
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
