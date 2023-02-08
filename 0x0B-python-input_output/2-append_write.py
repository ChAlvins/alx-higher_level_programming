#!/usr/bin/python3
""" Module that contains a function that appends to a text file
"""


def append_write(filename="", text=""):
    """ Function that appends to a text file
    If the file doesn’t exist, it should be created
    using the with statement
    no need to manage file permission or file doesn't exist exceptions.
    """

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
