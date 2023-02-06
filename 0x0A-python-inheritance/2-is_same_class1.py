#!/usr/bin/python3
"""a function that returns True if the object is exactly an instance
   of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """a function returning true or false"""

    return obj.__class__ == a_class
