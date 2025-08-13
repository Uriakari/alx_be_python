import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a fresh calculator before each test."""
        self.calc = SimpleCalculator()

    # ---------- Addition ----------
    def test_addition_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-4, -6), -10)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_floats(self):
        # Floating-point math -> use AlmostEqual
        self.assertAlmostEqual(self.calc.add(1.2, 3.4), 4.6, places=7)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)

    def test_addition_commutative(self):
        pairs = [(5, 7), (-3, 10), (0.5, 2.5)]
        for a, b in pairs:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), self.calc.add(b, a))

    # ---------- Subtraction ----------
    def test_subtraction_integers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(3, 10), -7)
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtraction_identity(self):
        self.assertEqual(self.calc.subtract(8, 0), 8)
        self.assertEqual(self.calc.subtract(0, 8), -8)

    # ---------- Multiplication ----------
    def test_multiplication_integers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(-4, -5), 20)

    def test_multiplication_by_zero(self):
        self.assertEqual(self.calc.multiply(0, 99), 0)
        self.assertEqual(self.calc.multiply(99, 0), 0)

    def test_multiplication_commutative(self):
        pairs = [(3, 7), (-2, 9), (0.5, 8)]
        for a, b in pairs:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.multiply(a, b), self.calc.multiply(b, a))

    # ---------- Division ----------
    def test_division_integers(self):
        # Expect a float in Python 3 division
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(-10, 5), -2.0)
        self.assertEqual(self.calc.divide(-10, -5), 2.0)

    def test_division_floats(self):
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0, places=7)
        self.assertAlmostEqual(self.calc.divide(1, 4), 0.25, places=7)

    def test_division_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0.0)

    def test_division_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    # ---------- Large numbers ----------
    def test_large_numbers(self):
        self.assertEqual(self.calc.add(10**10, 10**10), 2 * 10**10)
        self.assertEqual(self.calc.subtract(10**12, 1), 10**12 - 1)
        self.assertEqual(self.calc.multiply(10**6, 10**6), 10**12)
        self.assertEqual(self.calc.divide(10**12, 10**6), 10**6)

if __name__ == "__main__":
    unittest.main()
