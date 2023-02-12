#!/usr/bin/python3
"""
11. Student to disk and reload

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
                k = key
                v = value

                """
                return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__

    """ Public method """
    def reload_from_json(self, json):
        """
        k = key
        v = value

        """
        for k, v in json.items():
            setattr(self, k, v)
