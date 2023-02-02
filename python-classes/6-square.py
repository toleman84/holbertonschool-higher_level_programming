#!/usr/bin/python3
"""
6. Coordinates of a square
"""


class Square:
    """ init function """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or \
           type(value[0]) != int or type(value[1]) != int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    """ Public instance method """
    def area(self):
        return(self.__size**2)

    """  that prints in stdout the square with the character # """
    def my_print(self):
        [print('') for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(' ', end='') for j in range(0, self.__position[0])]
            [print('#', end='') for k in range(0, self.__size)]
            print('')

        if self.__size == 0:
            print('')
