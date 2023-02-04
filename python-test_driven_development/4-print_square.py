#!/usr/bin/python3
"""
3. Print square
"""


def print_square(size):

    """ function that prints a square with the character # """

    if isinstance(size, int) is not True:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif isinstance(size, float) is True and size < 0:
        raise TypeError('size must be an integer')
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')
            print()
