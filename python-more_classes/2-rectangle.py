#!/usr/bin/python3
"""doc for module"""


class Rectangle:
    """doc for class"""

    def __init__(self, width=0, height=0):
        """doc for init function"""
        self.height = height
        self.width = width

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
