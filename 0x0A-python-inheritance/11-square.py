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

    def area(self):
        '''returns area of rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''string representation of the rectangle'''
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    '''class Square that inherits from Rectangle'''

    def __init__(self, size):
        '''instatiation with size'''

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        '''area of sqaure'''
        return self.__size * self.__size

    def __str__(self):
        '''string representation of square'''
        return "[Square] {}/{}".format(self.__size, self.__size)
