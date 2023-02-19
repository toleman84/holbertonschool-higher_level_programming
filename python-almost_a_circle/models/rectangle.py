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

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """
        if isinstance(value, int) is not True:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y """
        if isinstance(value, int) is not True:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """ area """
        return self.height * self.width

    print_symbol = '#'

    def display(self):
        """ public method """
        if self.__width == 0 or self.__height == 0:
            print('')
            return

        for i in range(self.height):
            [print('', end='') for x in range(self.x)]
            [print('#', end='') for w in range(self.width)]
            print('')

    def __str__(self):
        """ return: """
        return('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height))

    def update(self, *args, **kwargs):
        """update dict"""
        if (len(args) == 0):
            for (key, value) in kwargs.items():
                if (key == 'id'):
                    self.id = value
                if (key == 'size'):
                    self.width = value
                    self.height = value
                if (key == 'x'):
                    self.x = value
                if (key == 'y'):
                    self.y = value
        else:
            length = len(args)
            i = 0
            if (length > i):
                self.id = args[0]
                i += 1
            if (length > i):
                self.width = args[1]
                self.height = args[1]
                i += 1
            if (length > i):
                self.x = args[2]
                i += 1
            if (length > i):
                self.y = args[3]

    def to_dictionary(self):
        """ dictionary """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
        }
