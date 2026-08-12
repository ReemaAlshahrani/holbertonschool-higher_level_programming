#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestCase class to test max_integer function logic and edge cases.
    """

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max value at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_default_empty_list(self):
        """Test calling the function without arguments."""
        self.assertIsNone(max_integer())

    def test_one_element_list(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.53, 6.33, -9.12, 15.2, 6.0]), 15.2)

    def test_ints_and_floats(self):
        """Test with a mix of integers and floats."""
        self.assertEqual(max_integer([1.53, 15, 6.33, -9, 6.0]), 15)

    def test_negative_numbers(self):
        """Test with a list of all negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_signed_numbers(self):
        """Test with a mix of positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 10, -20]), 10)

    def test_string(self):
        """Test with a single string."""
        self.assertEqual(max_integer("Holberton"), 't')

    def test_list_of_strings(self):
        """Test with a list of strings."""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertIsNone(max_integer(""))


if __name__ == '__main__':
    unittest.main()
