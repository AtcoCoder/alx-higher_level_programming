#!/usr/bin/python3
""" This module is for a function that
adds two numbers a and b
Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise
a TypeError exception with the message a must be an
integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
You are not allowed to import any module
"""


def add_integer(a, b=98):
    """ This function adds two numbers
    and returns their sum.
    The numbers must be integers
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (a + b)
