#!/usr/bin/python3
'''module with a subclass inheriting from BaseGeometry'''


class BaseGeometry:
    '''class with a public instance raising an exception'''

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''instance validating value'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''Rectangle class inheriting from BaseGeometry'''

    def __init__(self, width, height):
        '''instatiation'''

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
