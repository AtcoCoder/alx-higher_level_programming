#!/usr/bin/python3
"""
Write a function that prints a text with 2 new lines after each of
these characters: ., ? and :

Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with
the message text must be a string
There should be no space at the beginning or at the end of each
printed line
You are not allowed to import any module
"""


def text_indentation(text):
    """ This function prints text and leaves new lines.
    No space at the beginning and end of each line.
    """

    if text is None or type(text) != str:
        raise TypeError("text must be a string")
    newline = True
    for char in text:
        if char == " ":
            if newline is True:
                continue
        print(char, sep="", end="")
        newline = False
        if char == "." or char == "?" or char == ":":
            print("\n")
            newline = True
    return
