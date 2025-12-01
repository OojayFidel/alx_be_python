import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        # basic cases for add()
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-4, -6), -10)

    def test_subtraction(self):
        # basic cases for subtract()
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-4, -6), 2)

    def test_multiplication(self):
        # basic cases for multiply()
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_division(self):
        # normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 2), 4.5)
        # division by zero should return None
        self.assertIsNone(self.calc.divide(5, 0))

if __name__ == "__main__":
    unittest.main()
