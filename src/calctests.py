import unittest

from calc import Calc


class MyTestCase(unittest.TestCase):

    def test_instantiate_calc(self):
        calc = Calc()
        self.assertIsInstance(calc, Calc)

    def test_results_property_calc(self):
        calc = Calc()
        self.assertEqual(calc.result, 5)

    def test_addition_method_calc(self):
        calc = Calc()
        self.assertEqual(calc.add(2,3), 5)

if __name__ == "__main__":
    unittest.main()