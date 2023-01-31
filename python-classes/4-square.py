#!/usr/bin/python3
"""
4. Access and update private attribute
defines a square
"""


class Square:
    """ init function """
    def __init__(self, size=0):
        self.size = size

    """ property to retrieve it """
    def size(self):
        return(self.size)

    """ class Square difinition """
    def size(self, value):
        """ size of a side of square """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.size = size

    """ Public instance method """
    def area(self):
        if type(self.size) != int:
            raise TypeError("size must be an integer")
        return(self.size**2)
