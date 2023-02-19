#!/usr/bin/python3
"""
Python - Almost a circle

"""

import json
import csv


class Base:
    """ private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ adding the static method """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save file """
        if list_objs is None:
            with open('{}.json'.format(cls.__name__), 'w') as f:
                f.write(to_json_string([]))
        else:
            new_list = []
            with open('{}.json'.format(cls.__name__), 'w') as f:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())
                f.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ from """
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)
