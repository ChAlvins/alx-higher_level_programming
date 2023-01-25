#!/usr/bin/python3
"""defining a class Square"""


class Square:
    """square with private instance attribute; size"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiation of square
        args:
            size (int) of square
            position(int, int) of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieve square size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """set value to position"""
        if type(value) is not tuple or len(value) > 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns area of square"""
        return (self.__size) * (self.__size)

    def my_print(self):
        """prints in stdout the square with character #"""
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
