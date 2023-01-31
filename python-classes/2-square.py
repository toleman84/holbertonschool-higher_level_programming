#!/usr/bin/python3
"""
2. Size validation
defines a square
"""


class Square:
    """ class Square difinition """
    def __init__(self, size=0):
        """ size of a side of square """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
