#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for numbers in range(len(matrix)):
        new_matrix = numbers ** 2
    print(new_matrix)
    print(matrix)
