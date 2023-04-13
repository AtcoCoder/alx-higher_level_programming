#!/usr/bin/python3
"""Contains write_file function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written"""
    with open(filename, mode='w', encoding="utf-8") as a_file:
        num_of_chars = a_file.write(text)
        return num_of_chars


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt",
                               "This School is so cool!\n")
    print(nb_characters)
