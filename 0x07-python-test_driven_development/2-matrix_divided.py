#!/usr/bin/python3
"""
Classes: None
Functions: matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix and returns the result as new matrix

    Args:
        matrix: the matrix to be divided
        div: the divisor
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must a be a number
        ZeroDivisionError: division by zero
    Returns:
        a new matrix resulted from the division
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    row_len = len(matrix[0])
    new_matrix = []
    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(row) != row_len:
            raise TypeError('Each row of the matrix must have the same size')
        for ele in row:
            if not isinstance(ele, int) and not isinstance(ele, float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            if ele == 0 and div < 0:
                new_ele = 0.0
            else:
                new_ele = round(ele / div, 2)
            new_row.append(new_ele)
        new_matrix.append(new_row)
    return new_matrix

print(matrix_divided(23, 23, 23))
