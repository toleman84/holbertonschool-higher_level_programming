#!/usr/bin/python3
"""
2. Append to a file

"""


def append_write(filename="", text=""):

    """ function that appends a string """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
