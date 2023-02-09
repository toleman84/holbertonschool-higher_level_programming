#!/usr/bin/python3
"""
7. Integer validator

"""


class BaseGeometry:
    
    """ Public instance method: """
    def area(self):
        raise Exception('area() is not implemented')

    """ Public instance method: """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        else:
            self.name = value
