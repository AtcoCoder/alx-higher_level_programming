#!/usr/bin/python3
"""Functions:
    text_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', ':'

    Args:
        text (string): text
    Raises:
        TypeError: text must be a string
    Return:
        None
    """
    text_len = len(text)
    i = 0
    while i < text_len:
        char = text[i]
        print(char, end='')
        if char in ['.', '?', ':']:
            print('\n')
            i += 1
        i += 1
