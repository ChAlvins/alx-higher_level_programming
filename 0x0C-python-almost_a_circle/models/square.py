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

    def __str__(self):
        """return the print() and str() representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
           self.id, self.x, self.y, self.width)
