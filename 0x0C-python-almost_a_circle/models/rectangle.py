#!/usr/bin/python3
"""module defining a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing rectangle
        Args:
            width(int): private attribute width of the new Rectangle.
            height(int): private attribute The height of the new Rectangle.
            x (int): Private attribute for x value of the Rectangle
            y (int): private attribute for y value of Rectangle
            id (int): private attribute inherited from Base
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for wisth of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x attribute of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y attribute of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """set y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
