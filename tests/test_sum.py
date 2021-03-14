import unittest
from calc.app import sum as my_sum

class TestSum(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(my_sum(1, 2), 3)

    def test_negative(self):
        self.assertEqual(my_sum(-4, -2), -6)

    def test_mixed(self):
        self.assertEqual(my_sum(-9, 2), -7)

    def test_zero(self):
        self.assertEqual(my_sum(0, 0), 0)


if __name__ == '__main__':
    unittest.main()