#!/usr/bin/python3
"""
3. Area of a square
Write a class Square that defines a square by: (based on 2-square.py)
"""


class Square:
    """doc"""
    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
    def area(self):
        return self.size * self.size
