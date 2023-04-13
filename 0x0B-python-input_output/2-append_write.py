#!/usr/bin/python3
"""Contains append_write function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    and returns the number of characters added"""
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)


if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt",
                                       "This School is so cool!\n")
    print(nb_characters_added)
