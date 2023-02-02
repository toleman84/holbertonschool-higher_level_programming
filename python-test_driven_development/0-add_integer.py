#!/usr/bin/python3
"""
0. Integers addition
"""


def add_integer(a, b=98):
    """ must be first casted to integers if they are float """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    """ Returns an integer: the addition of a and b """
    try:
        return a + b
    except TypeError:
        if isinstance(b, int) is True:
            raise TypeError('a must be an integer')
        else:
            raise TypeError('b must be an integer')
