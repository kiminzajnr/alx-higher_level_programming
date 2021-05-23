#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """
            test for when all values of list are integers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4.5999]), 4.5999)

    def test_non(self):
        """
            make sure none is returned when list is empty
        """
        self.assertEqual(max_integer([]), None)

    def test_types(self):
        """
            raising errors when value are not integers
        """
        self.assertRaises(TypeError, max_integer, [1, 2, 3, "4"])
        self.assertRaises(TypeError, max_integer, ["holberton", 2, 3, 4])

    def test_values(self):
        """
            raising errors when value is not an integer
        """
        pass
