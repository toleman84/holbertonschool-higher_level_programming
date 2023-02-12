#!/usr/bin/python3
"""
10. Student to JSON with filter

"""


class Student:
    """ Public instance attributes """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ Public method: return dict """
    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            for elements in attrs:
                """
                getattr():
                returns the value of the named attribute of an object.
                hasattr():
                returns true/false if an object has the given attribute.
                """
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__
