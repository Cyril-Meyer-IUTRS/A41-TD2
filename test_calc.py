import unittest
from calc import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    # Tests unitaires pour tester les différentes fonctions
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

    # Test d'intégration pour tester l'interaction entre add et subtract
    def test_add_subtract_integration(self):
        result = subtract(add(10, 5), 3)
        self.assertEqual(result, 12)

    # Test fonctionnel pour vérifier le comportement global du module calc
    def test_calculator_functional(self):
        input_values = [1, 2, 3, 4, 5]
        expected_sum = 15
        expected_diff = 4  # 5 - 1

        sum_result = 0
        diff_result = input_values[-1] - input_values[0]

        for value in input_values:
            sum_result = add(sum_result, value)

        self.assertEqual(sum_result, expected_sum)
        self.assertEqual(diff_result, expected_diff)


if __name__ == '__main__':
    unittest.main()
