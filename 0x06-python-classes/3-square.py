#!/usr/bin/python3
"""defining a class named square"""


class Square:
    """
    class defined with a private
    instance attribute: size
    """
    def __init__(self, size=0):
        """
        Args:
            size: size of square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        finds area of square
        Returns: area of the square
        """
        return self.__size ** 2
