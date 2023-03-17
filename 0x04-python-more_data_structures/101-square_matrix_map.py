#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """ Takes in a matrix and squares each value of the matrix
    and returns it as a new matrix """
    return list(map(lambda x: list(map(lambda y: y * y, x)), matrix))
