#!/usr/bin/python3
"""
module defining the clas "Student"
"""


class Student:
    """class to create student instances"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a Student instance"""
        return self.__dict__
