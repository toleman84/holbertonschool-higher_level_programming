#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        for j in matrix[i]:
            new_matrix = j ** 2
        print(new_matrix)
        print(matrix)
