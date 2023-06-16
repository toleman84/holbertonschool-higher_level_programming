#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """test integer"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

        result2 = max_integer([1, 3, 4, 2])
        self.assertEqual(result2, 4)

        result3 = max_integer([1])
        self.assertEqual(result3, 1)

    def test_not_number(self):
        """test not number"""
        with self.assertRaises(TypeError):
            max_integer([1, 'a'])

if __name__ == "__main__":
    unittest.main()
