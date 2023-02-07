#!/usr/bin/python3
""" Module that contains a function that reads from a file"""

def read_file(filename=""):
    """ Function that reads from a file
    Args:
        filename: filename
    no need to manage file permission or file doesn't exist exceptions
    """

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
