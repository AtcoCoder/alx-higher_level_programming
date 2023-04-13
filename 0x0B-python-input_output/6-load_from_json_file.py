#!/usr/bin/python3
"""Contains load_from_json_file"""


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, mode='r', encoding="utf-8") as a_file:
        data = a_file.read()
        import json
        return json.loads(data)
