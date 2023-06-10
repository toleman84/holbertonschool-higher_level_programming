#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for value in range(len(matrix[row])):
            print("{:d}".format(matrix[row][value]), end='')
            if value < len(matrix[value]) - 1:
                print(end=' ')
        print()
