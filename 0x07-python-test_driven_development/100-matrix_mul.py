#!/usr/bin/python3
""" This Module includes a function that multiplies two matrices:
Prototype: def matrix_mul(m_a, m_b):
m_a and m_b must be validated with these requirements in this order
m_a and m_b must be an list of lists of integers or floats:"
"""


def matrix_mul(m_a, m_b):
    """ This function multiplies two matrices
    without using any library module
    to do so - LOL"""

    if m_a is None:
        raise TypeError("m_a must be a list")
    if m_b is None:
        raise TypeError("m_b must be a list")
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    for elt in m_a:
        if type(elt) != list:
            raise TypeError("m_a must be a list of lists")
    for elt in m_b:
        if type(elt) != list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_a == [[]]:
        raise ValueError("m_b can't be empty")
    for elt in m_a:
        for num in elt:
            if type(num) != int and type(num) != float:
                raise TypeError("m_a should contain only integers or floats")
    for elt in m_b:
        for num in elt:
            if type(num) != int and type(num) != float:
                raise TypeError("m_b should contain only integers or floats")
    size_a = len(m_a[0])
    for row in m_a:
        if len(row) != size_a:
            raise TypeError("each row of m_a must be of the same size")
    size_b = len(m_b[0])
    for row in m_b:
        if len(row) != size_b:
            raise TypeError("each row of m_b must be of the same size")
    if size_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Now do the multiplication:
    res = []
    for i in range(len(m_a)):
        item = 0
        for j in range(len(m_a[0])):
            item += (m_a[i][j] * m_b[j][i])
        res.append(item)

    return 5
