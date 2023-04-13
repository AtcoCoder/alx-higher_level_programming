#!/usr/bin/python3
""" pascal_triangle function module
"""


def pascal_triangle(n):
    """
         returns a list of lists of
         integers representing
         the Pascal's triangle
    """
    i = 0
    if n <= 0:
        return []
    triangle = [[1]]
    previous = []
    while i < n - 1:
        current_list = [1]
        for index in range(i):
            current_list += [previous[index] + previous[index + 1]]
        previous = current_list
        previous += [1]
        triangle.append(previous)
        i += 1
    return triangle
