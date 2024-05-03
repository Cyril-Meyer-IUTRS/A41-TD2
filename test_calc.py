import unittest
from calc import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 7), 10)
        self.assertEqual(add(-2, 2), 0)
        self.assertEqual(add(-5, -3), -8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-4, 2), -6)
        self.assertEqual(subtract(0, -10), 10)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-4, -2), 8)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 3), 3.333, places=3)
        self.assertAlmostEqual(divide(-6, 2), -3, places=3)
        self.assertRaises(ValueError, divide, 5, 0)


if __name__ == '__main__':
    unittest.main()
