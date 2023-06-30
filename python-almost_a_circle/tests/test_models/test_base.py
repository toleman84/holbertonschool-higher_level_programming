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
        """Test"""
        pass

    def test_id_given(self):
        """Test ids match when given"""
        self.assertTrue(Base(999), self.id == 999)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-80), self.id == -80)

    def test_id_not_given(self):
        """Test"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_private_attr_access(self):
        """Test private attr are not accessible"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_invalid_args(self):
        """Test"""
        with self.assertRaises(TypeError):
            Base(50, 50)

    def test_class(self):
        """Test class"""
        self.assertTrue(Base(100), self.__class__ == Base)


if __name__ == "__main__":
    unittest.main()
