#!/usr/bin/python3
"""
3. Area of a square
Write a class Square that defines a square by: (based on 2-square.py)
"""


class Square:
    """doc"""
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
