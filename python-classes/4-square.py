#!/usr/bin/python3
"""
4. Access and update private attribute
Write a class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """doc class"""
    def size(self):
        """doc"""
        return self.__size

    def size(self, value):
        """doc"""
        self.value = value

        if type(value) is not int:
            TypeError("size must be an integer")
        if value < 0:
            ValueError("size must be >= 0")

    def __init__(self, size=0):
        """Initialize self"""
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area doc"""
        return self.__size * self.__size
