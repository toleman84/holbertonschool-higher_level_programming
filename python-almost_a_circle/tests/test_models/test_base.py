#!/usr/bin/pytohn3
"""_summary_
"""
import unittest
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test_setUp(self):
        """_summary_
        """
        pass

    def test_id_given(self):
        """_summary_
        """
        self.assertTrue(Base(999), self.id == 999)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-80), self.id == -80)

    def test_id_not_given(self):
        """_summary_
        """
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_private_attr_access(self):
        """_summary_
        """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_invalid_args(self):
        """_summary_
        """
        with self.assertRaises(TypeError):
            Base(50, 50)

    def test_class(self):
        """_summary_
        """
        self.assertTrue(Base(100), self.__class__ == Base)

    def test_none_to_json_string(self):
        """_summary_
        """
        self.assertTrue(type(Base.to_json_string([None])) == str)
        self.assertTrue(Base.to_json_string([None]), "[]")

    def test_to_json_string(self):
        """_summary_
        """
        dict_a = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        dict_b = {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        str_dict_a = Base.to_json_string([dict_a, dict_b])
        self.assertTrue(type(dict_a) == dict)
        self.assertTrue(type(str_dict_a) == str)

    def test_empty_to_json_string(self):
        """_summary_
        """
        self.assertTrue(len(dict()) == 0)
        self.assertTrue(type(Base.to_json_string([dict()])) == str)
        self.assertTrue(Base.to_json_string([dict()]), "[]")

    def test_from_json_string(self):
        """_summary_
        """
        s0 = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        self.assertTrue(type(s0) == str)
        self.assertTrue(type(Base.from_json_string(s0)) == list)
        self.assertTrue(type(Base.from_json_string(s0)[0]) == dict)


if __name__ == "__main__":
    unittest.main()
