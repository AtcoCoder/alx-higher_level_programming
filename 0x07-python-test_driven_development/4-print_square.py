#!/usr/bin/python3
"""
Write a function that prints a square with the character #.

Prototype: def print_square(size):
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception
with the message size must be an integer
if size is less than 0, raise a ValueError exception with the
message size must be >= 0
if size is a float and is less than 0, raise a TypeError exception
with the message size must be an integer
You are not allowed to import any module
"""


def print_square(size):
    """This function prints a square
    Tests are created to ensure it works.
    It defines a Square."""

    if size == 0:
        return

    if type(size) != int or (type(size) == float and int(size) != size):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for line in range(size):
        print("#" * size)
    return
