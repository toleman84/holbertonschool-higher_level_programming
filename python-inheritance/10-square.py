#!/usr/bin/python3
"""
10. Square #1

"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        """ size must be private. No getter or setter """
        self.__size = size
        """ size must be a positive integer, validated by integer_validator """
        self.integer_validator('size', size)
        """ call superclass """
        super().__init__(size, size)
