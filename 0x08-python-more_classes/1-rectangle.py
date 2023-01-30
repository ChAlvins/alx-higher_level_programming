#!/usr/bin/python3
"""a module with a class named Rectangle"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        """instantiantion
        args:
            width: width of rectangle
            height: height of rectangle
        """

        self.__width = width
        self.__height = height

        @property
        def width(self):
            """getter for Private instance attribute: width"""

            return self.__width

        @width.setter
        def width(self, value):
            """setter for private instance attribute width"""

            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """getter for Private instance attribute: height"""

            return self.__height

        def height(self, value):
            """setter for private instance attribute height"""

            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
