#!/usr/bin/python3
"""
4. Only sub class of

"""


def inherits_from(obj, a_class):
    """ if the object is an instance of a class that inherited """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
