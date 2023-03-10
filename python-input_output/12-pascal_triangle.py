#!/usr/bin/python3
"""
12. Pascal's Triangle

"""


def pascal_triangle(n):
    """ returns a list of lists of integers """
    if n <= 0:
        return []
    """ tri = triangle (max 79 chars) """
    tri = [[1]]
    for rows in range(n-1):
        tri.append([a+b for a, b in zip([0] + tri[-1], tri[-1] + [0])])
    return tri
