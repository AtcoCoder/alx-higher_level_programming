#!/usr/bin/python3
"""Contains inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if object obj is an
    instance of class a_class
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
