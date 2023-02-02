#!/usr/bin/python3


def add_integer(a, b=98):

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    try:
        return a + b
    except TypeError:
        if isinstance(b, int) is False:
            raise TypeError('a must be an integer')
        else:
            raise TypeError('b must be an integer')
