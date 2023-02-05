#!/usr/bin/python3
"""
1. Divide a matrix
"""


def matrix_divided(matrix, div):

    """ must be a list of lists of integers or floats """
    if (isinstance(matrix, list) is not True or
            not all((isinstance(i, int) or
                    isinstance(i, float))
                    for i in [num for row in matrix for num in row])):
        raise TypeError('matrix must be a matrix (list of lists) of integers/'
                        'floats')

    """ must be of the same size """
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    """ must be a number (integer or float) """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    """ div can’t be equal to 0 """
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
