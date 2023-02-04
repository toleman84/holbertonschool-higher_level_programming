#!/usr/bin/python3
"""
2. Say my name
"""


def say_my_name(first_name, last_name=""):

    """ function that prints ... """
    if isinstance(first_name, str) is not True:
        raise TypeError('first_name must be a string')
    elif isinstance(last_name, str) is not True:
        raise TypeError('last_name must be a string')
    else:
        print('My name is {} {}'.format(first_name, last_name))
