#!/usr/bin/python3
"""_summary_
"""
import unittest
from models import rectangle
Rectangle = rectangle.Rectangle


class Test_rectangle(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test_all_atribute(self):
        """_summary_
        """
        attr = Rectangle(20, 30, 2, 3, 99)
        self.assertTrue(attr.width == 20)
        self.assertTrue(attr.heigth == 30)
        self.assertTrue(attr.x == 2)
        self.assertTrue(attr.y == 3)
        self.assertTrue(attr.id == 99)


if __name__ == "__main__":
    unittest.main()
