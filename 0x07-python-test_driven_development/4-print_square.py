#!/usr/bin/python3
"""Functions:
    print_square
"""


def print_square(size):
    """
    Prints a square

    Args:
        size: size of the square
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    Returns:
        None
    """
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError('size must be integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for steps in range(size):
        print('#' * size)
