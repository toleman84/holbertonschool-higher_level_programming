#!/usr/bin/python3
"""doc"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """doc"""
    def __init__(self, size):
        """doc"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """doc"""
        return self.__size * self.__size

    def __str__(self):
        """doc"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
