#!/usr/bin/python3
"""doc"""


class MyList(list):
    """that prints the list, but sorted (ascending sort)"""
    def print_sorted(self):
        """doc"""
        print(sorted(self))
