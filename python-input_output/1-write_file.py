#!/usr/bin/python3
"""doc"""


def write_file(filename="", text=""):
    """doc"""
    with open(filename, "r", encoding="utf-8") as file:
        file.write(text)
