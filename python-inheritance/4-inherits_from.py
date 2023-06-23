#!/usr/bin/python3
"""doc"""


def inherits_from(obj, a_class):
    """doc"""
    return isinstance(obj, a_class) and type(obj) != a_class
