#!/usr/bin/python3
"""_summary_
"""
import json


class Base:
    """_class will be the “base” of all other classes in this project_
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """_summary_

        Args:
            self (_type_): _self object_
            id (_type_, optional): _id_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """_summary_

        Args:
            list_dictionaries (_type_): _description_
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """_summary_

        Args:
            list_objs (_type_): _description_
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + '.json'
        objs = []
        if list_objs is not None:
            for ob in list_objs:
                objs.append(cls.to_dictionary(ob))

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(objs))
