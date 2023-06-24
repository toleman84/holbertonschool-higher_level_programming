#!/usr/bin/python3
"""doc"""
import json


def class_to_json(obj):
    """doc"""
    return json.dumps(obj.__dict__)
