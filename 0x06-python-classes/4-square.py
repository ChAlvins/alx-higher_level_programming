#!/usr/bin/python3
"""defining class named square"""


class Square:
    """square with a private instance attribute: size"""

    def __init__(self, size=0):
        """
        initializing the square
        args: size of side of the square
        """
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """getter of size
        returns: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
