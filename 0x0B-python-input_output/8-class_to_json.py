#!/usr/bin/python3
""" Class to JSON function module
"""


def class_to_json(obj):
    """arg: object ojb
       returns: the dictionary description with simple data
       structure(list, dictionary, string, integer and boolean)
    """
    return obj.__dict__
