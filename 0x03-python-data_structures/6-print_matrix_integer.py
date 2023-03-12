#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) > 0:
            for num in row[:-1]:
                print("{:d}".format(num), end=' ')
            print("{:d}".format(row[-1]))
        else:
            print()
