#!/usr/bin/python3
"""
doc
for
documentation
"""


def matrix_divided(matrix, div):
    """
    doc for function
    """
    if not isinstance(matrix, list) and not isinstance(matrix, int)\
            or not isinstance(matrix, list) and not isinstance(matrix, float):
        raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

    #Each row of the matrix must be of the same size:
    for len_matrix in matrix:
        if len(len_matrix) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # All elements of the matrix should be divided by div, rounded to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_matrix_2 = []
        for numbers in row:
            new_matrix_2.append(round(numbers / div), 2)
        new_matrix.append(new_matrix_2)

    return new_matrix
