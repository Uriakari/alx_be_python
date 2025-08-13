import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        # integers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-4, -6), -10)
        self.assertEqual(self.calc.add(0, 0), 0)
        # floats
        self.assertAlmostEqual(self.calc.add(1.2, 3.4), 4.6, places=7)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
        # commutativity
        for a, b in [(5, 7), (-3, 10), (0.5, 2.5)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), self.calc.add(b, a))
        # large numbers
        self.assertEqual(self.calc.add(10**10, 10**10), 2 * 10**10)

    def test_subtraction(self):
        # integers
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        # identities
        self.assertEqual(self.calc.subtract(8, 0), 8)
        self.assertEqual(self.calc.subtract(0, 8), -8)
        # floats
        self.assertAlmostEqual(self.calc.subtract(7.5, 2.5), 5.0, places=7)
        # large numbers
        self.assertEqual(self.calc.subtract(10**12, 1), 10**12 - 1)

    def test_multiplication(self):
        # integers
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        # zero
        self.assertEqual(self.calc.multiply(0, 99), 0)
        self.assertEqual(self.calc.multiply(99, 0), 0)
        # floats
        self.assertAlmostEqual(self.calc.multiply(0.5, 8), 4.0, places=7)
        # commutativity
        for a, b in [(3, 7), (-2, 9), (0.5, 8)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.multiply(a, b), self.calc.multiply(b, a))
        # large numbers
        self.assertEqual(self.calc.multiply(10**6, 10**6), 10**12)

    def test_division(self):
        # normal division
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(-10, 5), -2.0)
        self.assertEqual(self.calc.divide(-10, -5), 2.0)
        # floats
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0, places=7)
        self.assertAlmostEqual(self.calc.divide(1, 4), 0.25, places=7)
        # zero numerator
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        # division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == "__main__":
    unittest.main()
