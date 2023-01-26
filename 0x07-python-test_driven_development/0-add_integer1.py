#!/usr/bin/python3
"""Module "0-add_integer" that adds two integers (a, b)"""


def add_integer(a, b=98):
    """Return sum of two numbers."""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
