#!/usr/bin/python3
"""defining class square"""


class Square:
    """class with a private attribute: size"""

    def __init__(self, size=0):
        """iniatializing object"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
