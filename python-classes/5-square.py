#!/usr/bin/python3
"""
5. Printing a square
"""


class Square:
    """ init function """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        """ size of a side of square """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    """ Public instance method """
    def area(self):
#        if type(self.size) != int:
#            raise TypeError("size must be an integer")
        return(self.__size**2)

    """  that prints in stdout the square with the character # """
    def my_print(self):
        for i in range(0, self.__size):
            [print('#', end='') for j in range(self.__size)]
            print('')
        if self.__size == 0:
            print('')
