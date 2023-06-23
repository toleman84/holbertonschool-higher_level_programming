#!/usr/bin/python3
"""doc"""


def read_file(filename=""):
    """doc"""
    with open(filename, "r", encoding="utf8") as file:
        for lines in file:
            print(lines, end="")
