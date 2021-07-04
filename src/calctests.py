import unittest
from calc import Calc
from csvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calc()

    def test_instantiate_calc(self):
        self.assertIsInstance(self.calc, Calc)

    def test_results_property_calc(self):
        self.assertEqual(self.calc.result, 0)

    def test_addition_method_calc(self):
        test_files = CsvReader("/src/files/Unit Test Add.csv").get_data
        for row in test_files:
            self.assertEqual(self.calc.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calc.result, int(row['Result']))

    def test_subtraction_method_calc(self):
        test_files = CsvReader("/src/files/Unit Test Sub.csv").get_data
        for row in test_files:
            self.assertEqual(self.calc.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calc.result, int(row['Result']))

    def test_division_method_calc(self):
        test_files = CsvReader("/src/files/Unit Test Div.csv").get_data
        for row in test_files:
            self.assertAlmostEqual(self.calc.div(row['Value 2'], row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calc.result, float(row['Result']))

    def test_multiplication_method_calc(self):
        test_files = CsvReader("/src/files/Unit Test Mult.csv").get_data
        for row in test_files:
            self.assertEqual(self.calc.mult(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calc.result, int(row['Result']))

    def test_square_method_calc(self):
        test_files = CsvReader("/src/files/Unit Test Square.csv").get_data
        for row in test_files:
            self.assertAlmostEqual(self.calc.square(row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calc.result, float(row['Result']))

    def test_squareroot_method_calc(self):
        test_files = CsvReader("/src/files/Unit Test Square root.csv").get_data
        for row in test_files:
            self.assertAlmostEqual(self.calc.sqr_root(row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calc.result, float(row['Result']))

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
