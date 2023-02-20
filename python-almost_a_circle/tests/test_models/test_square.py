#!/usr/bin/python3
"""
test square

"""

import io
import unittest

from models.base import Base
from models.square import Square


class Test_instantiation(unittest.TestCase):

    def test_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)


class Test_size(unittest.TestCase):

    def test_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)


class Test_x(unittest.TestCase):

    def test_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")


class Test_y(unittest.TestCase):

    def test_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)


class Test_area(unittest.TestCase):

    def test_area(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())


class Test_update_args(unittest.TestCase):

    def test_update(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))


class Test_update_kwargs(unittest.TestCase):

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))


class Test_to_dictionary(unittest.TestCase):

    def test_to_dictionary(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()
