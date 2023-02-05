#!/usr/bin/python3
"""
8. Compare rectangles

"""


class Rectangle:

    """ Private instance attribute: width """

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError('width must be an integer')
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
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__height = value

    """ Instantiation with optional width and height: """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            string.append(str(self.print_symbol) * self.__width)
            string.append('\n')
        string.pop()
        return (''.join(string))

    def __repr__(self):
        return ('Rectangle({}, {})'
                .format(str(self.__width), str(self.__height)))

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    """ Static method  """

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif isinstance(rect_2, Rectangle) is not True:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        width = size
        height = size
        return cls(width, height)
