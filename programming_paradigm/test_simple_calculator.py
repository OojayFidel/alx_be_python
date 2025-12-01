import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    # ---- Tests for add() ----
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(5, 7), 12)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-3, -8), -11)

    def test_add_mixed_numbers(self):
        self.assertEqual(self.calc.add(-4, 10), 6)

    # ---- Tests for subtract() ----
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(self.calc.subtract(7, -3), 10)

    # ---- Tests for multiply() ----
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(8, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -6), 18)

    # ---- Tests for divide() ----
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_float(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
    unittest.main()
