#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_notint(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 1, 7])
            max_integer([1, 5, 9, 'bug'])

    def test_empty(self):
        self.assertIsNone(max_integer([]), "Expect None for empty list")

    def test_allPositive(self):
        self.assertEqual(max_integer([1, 3, 2, 4, 9]), 9, "Expect 5")

    def test_allNegative(self):
        self.assertEqual(max_integer([-7, -3, -2, -5]), -2, "Expected -2")

    def test_PositiveandNeg(self):
        self.assertEqual(max_integer([-1, 3, -2, 4, 0]), 4, "Expected 4 (max)")

    def test_NotUnique(self):
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3, "Expected 3")

    def test_singleItem(self):
        self.assertEqual(max_integer([-2030]), -2030, "expect -2030")

    def test_beginwith(self):
        self.assertEqual(max_integer([2030, 10, 20, 30, 1010]), 2030, "2030")


if __name__ == '__main__':
    unittest.main()
