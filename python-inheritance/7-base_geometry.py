#!/usr/bin/python3
"""doc"""


class BaseGeometry:
    """doc"""
    def area(self):
        """doc"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """doc"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
