#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats, otherwise raise a
TypeError exception with the message matrix must be a matrix (list of lists)
of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError
exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError exception
with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with
the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal
places
Returns a new matrix
You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    """ This function divides a matrix by a number
    The number must be a float or int.
    Returns a new matrix.
    """

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError(msg)
    if len(matrix) == 0:
        raise TypeError(msg)
    for elt in matrix:
        if type(elt) != list or len(elt) == 0:
            raise TypeError(msg)
    cols = len(matrix[0])
    for elt in matrix:
        if len(elt) != cols:
            raise TypeError("Each row of the matrix must have the same size")
        for num in elt:
            if (type(num) != int and type(num) != float):
                raise TypeError(msg)

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in rw] for rw in matrix]
