#!/usr/bin/python3
"""
1. Real definition of a rectangle

"""


class Rectangle:

    """ Private instance attribute: width: """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    """ Private instance attribute: height: """

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    """ Instantiation with optional width and height: """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
