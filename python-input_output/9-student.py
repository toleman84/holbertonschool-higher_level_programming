#!/usr/bin/python3
"""doc"""

class_to_json = __import__("8-class_to_json").class_to_json


class Student:
    """class Student that defines a student by:"""
    first_name = ""
    last_name = ""
    age = 0


    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation of a Student instance"""
        return self.__dict__
