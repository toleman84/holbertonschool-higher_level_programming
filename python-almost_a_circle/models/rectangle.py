#!/usr/bin/python3
"""
Python - Almost a circle

"""

from models.base import Base


class Rectangle(Base):
    """ Class constructor """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Private instance attributes """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, width):
        """ set width """
        if isinstance(width, int) is not True:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, height):
        """ get height """
        if isinstance(height, int) is not True:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    def area(self):
        """ area """
        return self.height * self.width

    print_symbol = '#'

    def display(self):
        """ public method """
        if self.__width == 0 or self.__height == 0:
            return ''
        string = []
        for i in range(self.__height):
            string.append(str(self.print_symbol) * self.__width)
            string.append('\n')
            string.pop()
        return (''.join(string))

    def __str__(self):
        """ return: """
        return('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height))

    def update(self, *args, **kwargs):
        """ public method """
        index = 0
        lenght = len(args)

        self.id = args[0]
        self.width = args[1]
        self.height = args[2]
        self.x = args[3]
        self.y = args[4]
