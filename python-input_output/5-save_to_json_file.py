#!/usr/bin/python3
"""doc"""
import json


def save_to_json_file(my_obj, filename):
    """doc"""
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(my_obj, file)
