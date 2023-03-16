#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # create a new matrix from the square of each value of matrix
    new_matrix = [[num ** 2 for num in matrix[i]] for i in range(len(matrix))]
    # return a new matrix same size as matrix
    return new_matrix
