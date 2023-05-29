#!/usr/bin/python3
"""Functions:
    matrix_mul
"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices

    Args:
        m_a (list): list of integers
        m_b (list): list of integers

    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for ele in m_a:
        if not isinstance(ele, list):
            raise TypeError('m_a must be a list of lists')
    for ele in m_b:
        if not isinstance(ele, list):
            raise TypeError('m_b must be a list of lists')
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for ele in row:
            if not isinstance(ele, int) and not isinstance(ele, float):
                raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        for ele in row:
            if not isinstance(ele, int) and not isinstance(ele, float):
                raise TypeError('m_b should contain only integers or floats')
    rows_a = len(m_a)
    rows_b = len(m_b)
    cols_a = len(m_a[0])
    cols_b = len(m_b[0])
    for row in m_a:
        if len(row) != cols_a:
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != cols_b:
            raise TypeError("each row of m_b must be of the same size")
    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    new_m = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                new_m[i][j] += m_a[i][k] * m_b[k][j]
    return new_m
