#!/usr/bin/python3
"""doc"""
import json


def load_from_json_file(filename):
    """doc"""
    with open(filename, "r") as file:
        return json.load(file)
