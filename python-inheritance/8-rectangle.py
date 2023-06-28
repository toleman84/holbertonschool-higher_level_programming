#!/usr/bin/python3
"""doc"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """doc"""
    def __init__(self, width, height):
        """doc"""
        self.__width = width
        self.__heigth = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
