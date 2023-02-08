#!/usr/bin/python3
"""adds a new attribute to an object
if it’s possible
"""


def add_attribute(obj, attribute, value):
    """a function that adds a new attribute to an object"""

    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
