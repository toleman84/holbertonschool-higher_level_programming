#!/usr/bin/python3
"""doc"""


def append_write(filename="", text=""):
    """doc"""
    with open(filename, "a", encoding="utf-8") as file:
        numbers = file.write(text)
        return numbers
