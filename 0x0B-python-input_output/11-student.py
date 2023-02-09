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

    def to_json(self, attrs=None):
        """Represents of Student into json format
        Return: Student class as a json format"""

        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """Represents of Student into json format
        Attributes:
            attrs (dict): A python object to convert
        Return:
            Student class as a json format
        """

        for key, value in json.items():
            setattr(self, key, value)
