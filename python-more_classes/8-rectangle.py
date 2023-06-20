#!/usr/bin/python3
"""doc for module"""


class Rectangle:
    """doc for class"""

    """Public class attribute number_of_instances: Initialized to 0"""
    number_of_instances = 0
    """Public class attribute print_symbol: Initialized to #"""
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """doc for init function"""
        self.height = height
        self.width = width

        """Incremented during each new instance instantiation"""
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set it:"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set it:"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """that returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """that returns the rectangle perimeter:"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """should print the rectangle with the character #"""
        a = ""
        if self.width == 0 or self.height == 0:
            return a
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    a += str(self.print_symbol)
                a += "\n"
            return a[:-1]

    def __repr__(self) -> str:
        """return a string representation of the rectangle by using eval()"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Print the message Bye rectangle..."""
        print("Bye rectangle...")

        """Decremented during each instance deletion"""
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """that returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        # if both have the same area value
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
