#!/usr/bin/python3
"""
a module with a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """function args:
                    first_name: a string
                    last_name: a string
    Raises:
            TypeError: if args not strings
    """

    if type(first_name) is not str:
        raise TypeErorr("first_name must be string")

    if type(last_name) is not str:
        raise TypeError("last_name must be string")

    print("My name is {} {}".format(first_name, last_name))
