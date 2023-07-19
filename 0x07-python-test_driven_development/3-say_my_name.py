#!/usr/bin/python3
"""Funstions:
    say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the string 'My name is <first name> <last name>'

    Args:
        first_name: first name
        last_name: last name
    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    Return:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
