#!/usr/bin/python3
"""
5. Detect instance deletion

"""


class Rectangle:

    """ Private instance attribute: width """

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError('Width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    """ Private instance attribute: height """

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError('Width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__height = value

    """ Instantiation with optional width and height: """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ Public instance method: """

    def area(self):
        return self.height * self.width

    """ Public instance method: """

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        string = []
        for i in range(self.__height):
            string.append('#' * self.__width)
            string.append('\n')
        string.pop()
        return (''.join(string))

    def __repr__(self):
        return ('Rectangle({}, {})'
                .format(str(self.__width), str(self.__height)))

    def __del__(self):
        print('Bye rectangle...')
