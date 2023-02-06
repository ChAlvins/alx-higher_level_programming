#!/usr/bin/python3
'''module with a class'''


class BaseGeometry:
    '''class with a public instance raising an exception'''

    def area(self):
        raise Exception('area() is not implemented')
