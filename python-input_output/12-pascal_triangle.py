#!/usr/bin/python3
"""doc"""


def pascal_triangle(n):
    """doc"""
    if n <= 0:
        return []

    tri = [[1]]
    for rows in range(n-1):
        tri.append([a+b for a, b in zip([0] + tri[-1], tri[-1] + [0])])
    return tri
