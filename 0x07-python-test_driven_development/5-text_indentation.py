#!/usr/bin/python3
"""
Module composed by a function that prints 2 new lines after ".?:" characters
"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters
    Args:
        text: string
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        print(i, end="")
        if i in [".", "?", ":"]:
            print("\n")
