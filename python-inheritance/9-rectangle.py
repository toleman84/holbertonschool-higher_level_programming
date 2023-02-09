#!/usr/bin/python3
"""
8. Rectangle

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """ Instantiation with width and height """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        prints = '[' + str(self.__class__.__name__) + '] '
        prints += str(self.__width) + '/' + str(self.__height)
        return prints
