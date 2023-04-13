#!/usr/bin/python3
"""Contains a script that adds all arguments to a Python list
and the save them to a file."""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

python_list = []
try:
    python_list += load_from_json_file("add_item.json")
except FileNotFoundError:
    pass

for arg in sys.argv[1:]:
    python_list.append(arg)

save_to_json_file(python_list, "add_item.json")
