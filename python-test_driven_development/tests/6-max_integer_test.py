#!/usr/bin/python3

"""
5. Max integer - Unittest

"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_one(self):
        self.assertEqual(max_integer([4]), 4)

    def test_two(self):
        self.assertEqual(max_integer("stef"), "t")

    def test_empty(self):
        self.assertEqual(max_integer([None]), None)

    def test_str(self):
        self.assertEqual(max_integer(["stef", "cat", "is"]), "stef")

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, 4]), 4)

if __name__ == '__main__':
    unittest.main()
