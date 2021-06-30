import unittest
from calc import Calc


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calc()

    def test_instantiate_calc(self):
        self.assertIsInstance(self.calc, Calc)

    def test_results_property_calc(self):
        self.assertEqual(self.calc.result, 0)

    def test_addition_method_calc(self):
        self.assertEqual(self.calc.add(2,3), 5)
        self.assertEqual(self.calc.result, 5)

    def test_subtraction_method_calc(self):
        self.assertEqual(self.calc.subtract(7,4), 3)
        self.assertEqual(self.calc.result, 3)

    def test_division_method_calc(self):
        self.assertEqual(self.calc.div(9,3), 3)
        self.assertEqual(self.calc.result, 3)

    def tearDown(self) -> None:
        pass

if __name__ == "__main__":
    unittest.main()