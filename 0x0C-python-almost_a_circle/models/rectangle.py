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

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end=' ')
            print()

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        Args:
            *args (ints): New attribute values
            1st argument represents id attribute
            2nd argument represents width attribute
            3rd argument represent height attribute
            4th argument represents x attribute
            5th argument represents y attribute
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == 'width':
                    self.width = v
                elif k == 'height':
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of the rectangle"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
