#!/usr/bin/python3
"""
a module with a function that prints a square with the character #
"""


def print_square(size):
    """
    function printing square in #
    arg: size which size length of the square
    raises:
        TypeError
        valueError
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    '''
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    '''

    for i in range(size):
        print("#" * size)
