import unittest


def factorize(x):
    """ Factorize integer positive and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """
    if not isinstance(x, int):
        raise TypeError
    elif x < 0:
        raise ValueError


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        cases = ('string', 1.5)
        for c in cases:
            with self.subTest(x=c):
                self.assertRaises(TypeError, factorize, c)

    def test_negative(self):
        cases = (-1, -10, -100)
        for c in cases:
            with self.subTest(x=c):
                self.assertRaises(ValueError, factorize, c)

    def test_zero_and_one_cases(self):
        cases = (0, 1)
        for c in cases:
            with self.subTest(x=c):
                a = factorize(c)
                self.assertEqual(a, (c,))

    def test_simple_numbers(self):
        cases = (3, 13, 29)
        for c in cases:
            with self.subTest(x=c):
                a = factorize(c)
                self.assertEqual(a, (c,))

    def test_two_simple_multipliers(self):
        cases = {6: (2, 3), 26: (2, 13), 121: (11, 11)}
        for c in cases.keys():
            with self.subTest(x=c):
                a = factorize(c)
                self.assertEqual(a, cases[c])

    def test_many_multipliers(self):
        cases = {1001: (7, 11, 13), 9699690: (2, 3, 5, 7, 11, 13, 17, 19)}
        for c in cases.keys():
            with self.subTest(x=c):
                a = factorize(c)
                self.assertEqual(a, cases[c])
