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

    def test_multiplication_method_calc(self):
        self.assertEqual(self.calc.mult(3,4), 12)
        self.assertEqual(self.calc.result, 12)

    def test_square_method_calc(self):
        self.assertEqual(self.calc.square(5), 25)
        self.assertEqual(self.calc.result, 25)

    def test_squareroot_method_calc(self):
        self.assertEqual(self.calc.square_root(36), 6)
        self.assertEqual(self.calc.result, 6)

    def tearDown(self) -> None:
        pass

if __name__ == "__main__":
    unittest.main()