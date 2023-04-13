#!/usr/bin/python3
"""Contains from_json_string function"""


def from_json_string(my_str):
    """Returns an object represented by a JSON string"""
    import json
    return json.loads(my_str)
