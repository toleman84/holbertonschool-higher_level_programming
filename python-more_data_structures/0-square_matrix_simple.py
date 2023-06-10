#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        for j in i:
            new_matrix.append(j ** 2)
    print(new_matrix)
