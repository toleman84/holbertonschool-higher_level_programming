#!/usr/bin/python3
"""from json string to json object"""
import json


def from_json_string(my_str):
    """return a json object"""
    return json.loads(my_str)
