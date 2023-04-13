#!/usr/bin/python3
"""
    append_after function module
"""


def append_after(filename="", search_string="", new_string=""):
    """
        inserts a line of text to file [filename]
        after each line containing a specfic string [search_string]
    """
    list_of_lines = ""
    with open(filename, mode='r', encoding="utf-8") as a_file:
        for line in a_file:
            list_of_lines += line
            if search_string in line:
                list_of_lines += new_string
    with open(filename, mode='w', encoding="utf-8") as a_file:
        a_file.write(list_of_lines)


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
