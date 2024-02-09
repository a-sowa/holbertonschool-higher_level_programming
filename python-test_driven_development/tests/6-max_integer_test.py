#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Test when the list has regular positive integers """
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 5, 8, 12]), 12)

    """ Test when the list is empty """
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    """ Test when the list has negative numbers """
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)
        self.assertEqual(max_integer([-10, -5, -8, -12]), -5)

    """ Test when the list has duplicate maximum values """
    def test_duplicate_max(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    """ Test when the list has mixed positive, negative, and zero values """
    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, 0]), 3)
        self.assertEqual(max_integer([-1, -2, -3, 0]), 0)

    """ Test when the list has a single element """
    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    """ Test when the list has float numbers """
    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 2.0]), 3.5)

if __name__ == '__main__':
    unittest.main()
