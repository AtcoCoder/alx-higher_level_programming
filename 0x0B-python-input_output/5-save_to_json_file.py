#!/usr/bin/python3
"""Contains save_to_json_file function"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file,
    using a JSON representation"""
    with open(filename, mode='w', encoding="utf-8") as a_file:
        import json
        data = json.dumps(my_obj)
        a_file.write(data)
