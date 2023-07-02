#!/usr/bin/python3
"""_summary_
"""
import unittest
from models import square
Square = square.Square


class Test_square(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test_all_atribute(self):
        """_summary_
        """
        attr = Square(20, 2, 3, 99)
        self.assertTrue(attr.width == 20)
        self.assertTrue(attr.heigth == 20)
        self.assertTrue(attr.size == 20)
        self.assertTrue(attr.x == 2)
        self.assertTrue(attr.y == 3)
        self.assertTrue(attr.id == 99)

    def test_one_atribute(self):
        """_summary_
        """
        attr = Square(20)
        self.assertTrue(attr.width == 20)
        self.assertTrue(attr.heigth == 20)
        self.assertTrue(attr.size == 20)
        self.assertTrue(attr.x == 0)
        self.assertTrue(attr.y == 0)
        self.assertTrue(attr.id is not None)

    def test_validated_attr(self):
        """_summary_
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("9")
            Square([20, 30])
            Square({20, })
            Square({"k": 20})
            Square(None)
            Square((20, 30), 99)

    def test_validated_integer(self):
        """_summary_
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
            Square(9).size(-9)

    def test_invalid_args(self):
        """_summary_
        """
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7, 8, 9)
            
    def test_class(self):
        """_summary_
        """
        self.assertEqual(type(Square(9)), Square)

    def test_area(self):
        """_summary_
        """
        self.assertEqual(Square(2).area(), 4)
        self.assertEqual(Square(5, 0, 0).area(), 25)

#    def test_display(self):

    def test_print(self):
        """_summary_
        """
        s = Square(1, 2, 3, 99)
        s.size = 900
        self.assertEqual(str(s), '[Square] (99) 2/3 - 900')

    def test_update(self):
        """_summary_
        """
        s = Square(1, 2, 3, 4)
        s.update(10, 10, 10, 10)
        self.assertEqual(str(s), '[Square] (10) 10/3 - 10')
        s.update(99)
        self.assertEqual(str(s), '[Square] (99) 10/3 - 10')

    def test_to_dictionary(self):
        """_summary_
        """
        sdic = Square(1, 2, 3, 4).to_dictionary()
        self.assertEqual(str(sdic), "{'id': 4, 'size': 1, 'x': 2, 'y': 3}")


if __name__ == "__main__":
    unittest.main()
