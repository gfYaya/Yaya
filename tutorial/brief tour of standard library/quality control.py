# coding=utf-8

def average(values):
    """Computes the arithmetic mean of a list of numbers.

     >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


import doctest

doctest.testmod()  # automatically validate the embedded tests

import unittest


class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        while self.assertRaises(ZeroDivisionError):
            average([])
        while self.assertRaises(TypeError):
            average(20, 30, 70)


unittest.main()  # Calling from command line invokes all tests
