#!/usr/bin/python3
"""module with BaseGeometry class"""


class BaseGeometry:
    """Base Geometry class empty"""

    def area(self):
        """Area output"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ that validates value"""

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """Empty rectangle class"""

    def __init__(self, width, height):
        """ constructor that takes two arguments:
        width and height."""

        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)

    def area(self):
        """area output"""

        return self.__width * self.__height

    def __str__(self):
        """method returns a string representation
        of the rectangle
        """

        return f'[Rectangle] {self.__width}/{self.__height}'


class Square(Rectangle):
    """Empty square class"""

    def __init__(self, size):
        """a constructor that takes a single argument: size."""

        super().__init__(size, size)

    def area(self):
        """area output"""

        return self.__width * self.__height
