#!/usr/bin/python3
"""
mode with a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """function
    args: first_name is a str
          last_name is a str
    Raise:
        Typeerror: if args not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
