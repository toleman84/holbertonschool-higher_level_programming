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

    for len_matrix in matrix:
        if len(len_matrix) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix_2 = []
        for numbers in row:
            result = numbers / div
            new_matrix_2.append(round(result, 2))
        new_matrix.append(new_matrix_2)

    return new_matrix
