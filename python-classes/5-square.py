#!/usr/bin/python3
"""
4. Access and update private attribute
Write a class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """doc class"""
    @property
    def size(self):
        """doc"""
        return self.__size

    @size.setter
    def size(self, value):
        """doc"""
        self.__size = value

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

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

    def my_print(self):
        """print doc"""
        if self.__size == 0:
            print()        
        for i in range(self.__size):
            print("#")
