import my_math
import unittest


class TestFact(unittest.TestCase):
    def test_fact_0(self):
        self.assertEqual(my_math.fact(0), 1)

    def test_fact_1(self):
        self.assertEqual(my_math.fact(1), 1)

    def test_negative_vals(self):
        with self.assertRaises(ValueError):
            my_math.fact(-1)

    def test_float_numbers(self):
        with self.assertRaises(TypeError):
            my_math.fact(1.66)


if __name__ == '__main__':
    unittest.main()
