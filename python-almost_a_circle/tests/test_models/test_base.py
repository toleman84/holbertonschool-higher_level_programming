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

    def test_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(isinstance(r1_dictionary, dict), True)
        self.assertEqual(str(r1_dictionary), "{'id': 5, 'width': 10, \
'height': 2, 'x': 1, 'y': 9}")
        self.assertEqual(str(type(r1_dictionary)), "<class 'dict'>")

    def test_dictionary_s1(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(str(s1_dictionary), "{'id': 6, 'size': 10, \
'x': 2, 'y': 1}")


class Test_save_to_file(unittest.TestCase):

    @classmethod
    def test_file(self):
        """ test file """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

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

    def test_create_2(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)


class Test_load_from_file(unittest.TestCase):

    def test_load_from_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)


if __name__ == "__main__":
    unittest.main()
