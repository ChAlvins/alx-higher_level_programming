#!/usr/bin/python3
"""module defining a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a sqaure class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing square
        Args:
            size(int): size of the new square.
            x (int): attribute for x value of the square
            y (int): attribute for y value of square
            id (int): identity of the square
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigning attributes
        Args:
            *args (ints): list of args-no keyworded args
            1st argument represents id attribute
            2nd argument represents size attribute
            3rd argument represents x attribute
            4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """return the print() and str() representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
           self.id, self.x, self.y, self.width)
