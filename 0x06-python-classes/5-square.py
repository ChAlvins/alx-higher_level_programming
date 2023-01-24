#!/usr/bin/python3
"""defining class named square"""


class Square:
    """Square with private instance attribute size"""

    def __init__(self, size=0):
        """instantiantion
        args: size of square side
        """
        self.__self = size

    def area(self):
        """returns square area"""
        return (self.__size) ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        args: value (int): size of square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints in stdout the square with character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * (self.__size))
