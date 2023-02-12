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
                return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
