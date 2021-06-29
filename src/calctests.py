import unittest

from calc import Calc


class MyTestCase(unittest.TestCase):

    def test_instantiate_calc(self):
        calc = Calc()
        self.assertIsInstance(calc, Calc)


if __name__ == "__main__":
    unittest.main()