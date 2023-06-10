#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix2 = []
        for j in i:
            new_matrix2.append(j ** 2)
        new_matrix.append(new_matrix2)
    print(new_matrix)
