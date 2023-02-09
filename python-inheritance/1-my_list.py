#!/usr/bin/python3
"""
1. My list

"""


class MyList(list):

    """ public instance method """
    def print_sorted(self):
        """ that prints the list, but sorted (ascending sort) """
        print(sorted(self))
