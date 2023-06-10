#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix_2 = []
        for numbers in row:
            new_matrix_2.append(numbers ** 2)
        new_matrix.append(new_matrix_2)
    return new_matrix
