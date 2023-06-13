#!/usr/bin/python3
"""
4. Access and update private attribute
Write a class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """doc class"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and optional position:"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """doc"""
        return self.__size

    @size.setter
    def size(self, value):
        """doc"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """to retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        """doc"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area doc"""
        return self.__size * self.__size

    def my_print(self):
        """print doc"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
