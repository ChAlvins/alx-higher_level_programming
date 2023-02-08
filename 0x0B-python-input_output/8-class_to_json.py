#!/usr/bin/python3
"""serialize an object"""


def class_to_json(obj):
    """Use the built-in function vars to
    get the object's attributes"""

    return vars(obj)
