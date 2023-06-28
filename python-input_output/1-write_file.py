#!/usr/bin/python3
"""doc"""


def write_file(filename="", text=""):
    """doc"""
    with open(filename, "w", encoding="utf-8") as file:
        numbers = file.write(text)
        return numbers
