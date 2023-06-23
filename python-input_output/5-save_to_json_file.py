#!/usr/bin/python3
"""doc"""
import json


def save_to_json_file(my_obj, filename):
    """doc"""
    with open(filename, "w") as file:
        json.load(my_obj, file)
