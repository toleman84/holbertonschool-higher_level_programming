#!/usr/bin/python3

"""
5. Max integer - Unittest

"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_one(self):
        self.assertEqual(max_integer([4]), 4)

    def test_empty(self):
        self.assertEqual(max_integer([None]), None)

#    def test_str(self):
#        self.assertEqual(max_integer(["Chateau", "the", "cat", "is"]), "Chateau")

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_max_at_begginning(self):
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

if __name__ == '__main__':
    unittest.main()
