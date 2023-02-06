#!/usr/bin/python3
'''module with a class'''


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
