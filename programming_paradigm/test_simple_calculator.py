# programming_paradigm/test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_with_negative(self):
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_addition_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    # --- Subtraction Tests ---
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtraction_result_negative(self):
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_subtraction_with_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # --- Multiplication Tests ---
    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_with_negative(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calc.multiply(7, 0), 0)

    # --- Division Tests ---
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_with_float_result(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
