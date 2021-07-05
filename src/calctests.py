import unittest
from calc import Calc
from csvReader import CsvReader
from StaticVariable import StaticVariable

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calc()

    def test_instantiate_calc(self):
        self.assertIsInstance(self.calc, Calc)

    def test_results_property_calc(self):
        self.assertEqual(self.calc.result, 0)

    def test_addition_method_calc(self):
        test_files = CsvReader(StaticVariable.unit_Test_Add).get_data
        for row in test_files:
            self.assertEqual(self.calc.add(row[StaticVariable.value_1], row[StaticVariable.value_2]), int(row[StaticVariable.result]))
            self.assertEqual(self.calc.result, int(row[StaticVariable.result]))

    def test_subtraction_method_calc(self):
        test_files = CsvReader(StaticVariable.unit_Test_Sub).get_data
        for row in test_files:
            self.assertEqual(self.calc.subtract(row[StaticVariable.value_1], row[StaticVariable.value_2]), int(row[StaticVariable.result]))
            self.assertEqual(self.calc.result, int(row[StaticVariable.result]))

    def test_division_method_calc(self):
        test_files = CsvReader(StaticVariable.unit_Test_Div).get_data
        for row in test_files:
            self.assertAlmostEqual(self.calc.divide(row[StaticVariable.value_2], row[StaticVariable.value_1]), float(row[StaticVariable.result]))
            self.assertAlmostEqual(self.calc.result, float(row[StaticVariable.result]))

    def test_multiplication_method_calc(self):
        test_files = CsvReader(StaticVariable.unit_Test_Mult).get_data
        for row in test_files:
            self.assertEqual(self.calc.multiply(row[StaticVariable.value_1], row[StaticVariable.value_2]), int(row[StaticVariable.result]))
            self.assertEqual(self.calc.result, int(row[StaticVariable.result]))

    def test_square_method_calc(self):
        test_files = CsvReader(StaticVariable.unit_Test_Square).get_data
        for row in test_files:
            self.assertAlmostEqual(self.calc.square(row[StaticVariable.value_1]), float(row[StaticVariable.result]))
            self.assertAlmostEqual(self.calc.result, float(row[StaticVariable.result]))

    def test_squareroot_method_calc(self):
        test_files = CsvReader(StaticVariable.unit_Test_SquareRoot).get_data
        for row in test_files:
            self.assertAlmostEqual(self.calc.squareroot(row[StaticVariable.value_1]), float(row[StaticVariable.result]))
            self.assertAlmostEqual(self.calc.result, float(row[StaticVariable.result]))

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
