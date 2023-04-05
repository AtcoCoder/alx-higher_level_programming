#!/usr/bin/python3
""" This module says my name.
Write a function that prints My name is <first name> <last name>

Prototype: def say_my_name(first_name, last_name=""):
first_name and last_name must be strings otherwise,
raise a TypeError exception with the message first_name must
be a string or last_name must be a string
You are not allowed to import any module
"""


def say_my_name(first_name, last_name=""):
    """ This function says my name:
    First Name
    Last Name
    """

    if first_name is None or type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
    return
