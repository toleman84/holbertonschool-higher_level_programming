#!/usr/bin/python3
"""
test rectangle

"""

import unittest
import json

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_instantiation(unittest.TestCase):

    def test_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)


class Test_width(unittest.TestCase):

    def test_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)


class Test_height(unittest.TestCase):

    def test_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)


class Test_x(unittest.TestCase):

    def test_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)


class Test_y(unittest.TestCase):

    def test_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)


class Test_area(unittest.TestCase):

    def test_area(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())


class Test_update_args(unittest.TestCase):

    def test_update(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))


class Test_update_kwargs(unittest.TestCase):

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))


class Test_to_dictionary(unittest.TestCase):

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == '_main__':
    unittest.main()
