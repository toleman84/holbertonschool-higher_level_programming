#!/usr/bin/python3
"""
2. Size validation
Write a class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    """
    Attributes:
        size
    """
    def __init__(self, size=0):
        """function constructor"""
        self.__size = size

        if type(size) is int:
            pass
        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
