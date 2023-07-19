#!/usr/bin/python3
"Add: function module"


def add_integer(a, b=98):
    """
    Adds two inputs and returns the sum
    Args:
        a (int): first integer
        b (int): second integer with default value of 98
    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer
        ValueError: cannot convert float NaN to integer
    Returns:
        The sum of a and b
    """
    if not isinstance(a, int):
        if type(a) != float:
            raise TypeError('a must be an integer')
        elif a == float('nan'):
            raise ValueError('Cannot convert float NaN to integer')
        else:
            a = int(a)
    elif not isinstance(b, int):
        if type(b) != float:
            raise TypeError('b must be an integer')
        elif b == float('nan'):
            raise ValueError('Cannot convert float NaN to integer')
        else:
            b = int(b)
    return a + b
