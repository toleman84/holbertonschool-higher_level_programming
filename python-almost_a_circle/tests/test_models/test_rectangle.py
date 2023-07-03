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
        self.assertTrue(attr.height == 30)
        self.assertTrue(attr.x == 2)
        self.assertTrue(attr.y == 3)
        self.assertTrue(attr.id == 99)

    def test_default_atribute(self):
        """_summary_
        """
        attr = Rectangle(20, 30)
        self.assertTrue(attr.width == 20)
        self.assertTrue(attr.height == 30)
        self.assertTrue(attr.x == 0)
        self.assertTrue(attr.y == 0)
        self.assertTrue(attr.id is not None)

    def test_attr_validated(self):
        """_summary_
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("20", 30, 2, 3, 99)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(20, {"d": 30}, 2, 3, 99)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(20, 30, None, 3, 99)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(20, 30, 2, (3, 4), 99)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 30, 2, 3, 99)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(20, -30, 2, 3, 99)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(20, 30, -2, 3, 99)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(20, 30, 2, -3, 99)

    def test_invalid_args(self):
        """_summary_
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_class(self):
        """_summary_
        """
        self.assertEqual(type(Rectangle(2, 3)), Rectangle)

    def test_area(self):
        """_summary_
        """
        self.assertEqual(Rectangle(2, 3).area(), 6)
        self.assertEqual(Rectangle(2, 3, 0, 0).area(), 6)
        self.assertEqual(Rectangle(2, 3, 0, 0, 12).area(), 6)

    def test_print(self):
        """_summary_
        """
        r = Rectangle(20, 30, 2, 3, 99)
        self.assertEqual(str(r), '[Rectangle] (99) 2/3 - 20/30')

    def test_to_dictionary(self):
        """_summary_
        """
        rdic = Rectangle(20, 30, 2, 3, 99).to_dictionary()
        self.assertEqual(type(rdic), dict)
        r2 = Rectangle(10, 10)
        r2.update(**rdic)
        self.assertEqual(str(r2), '[Rectangle] (99) 2/3 - 20/30')


if __name__ == "__main__":
    unittest.main()
