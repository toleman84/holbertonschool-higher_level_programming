#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not key:
        return a_dictionary
    a_dictionary.update({key})
    return a_dictionary
