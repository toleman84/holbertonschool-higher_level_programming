#!/usr/bin/python3
"""
test base

"""

import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_instantiation(unittest.TestCase):

    """
    example:

    def test_upper(self):
        self.asserEqual('foo'.upper(), 'FOO')

    """

    def test_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)


class Test_to_json_string(unittest.TestCase):

    def test_to_json_string(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_dict(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(str(r1_dictionary), "{'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9}")

    def test_di(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(str(s1_dictionary), "{'id': 4, 'size': 10, 'x': 2, 'y': 1}")

class Test_save_to_file(unittest.TestCase):

    def test_save_to_file(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())


class Test_from_json_string(unittest.TestCase):

    def test_from_json_string(self):
        self.assertEqual([], Base.from_json_string(None))


class Test_create(unittest.TestCase):

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))


class Test_load_from_file(unittest.TestCase):

    def test_load_from_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

"""
class Test_save_to_file_csv(unittest.TestCase):


class Test_load_from_file_csv(unittest.TestCase):
"""


if __name__ == "__main__":
    unittest.main()
