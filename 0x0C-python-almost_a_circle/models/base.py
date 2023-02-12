#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C.
    Attributes:
        __nb_objects (int): private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args: id (int): The identity of the new Base.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries:"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        args:
            list_objs: is a list of instances who inherits of Base
        Return: json object to save in file
        """
        filename = cls.__name__ + ".json"
        string = []
        if list_objs is not None:
            for i in list_objs:
                string.append(cls.to_dictionary(i))
        with open(filename, "w", encoding="utf-8") as jsonfile:
            jsonfile.write(cls.to_json_string(string))

    @staticmethod
    def from_json_string(json_string):
        """eturns the list of the JSON string representation json_string:
        args:
            json_string: s a string representing a list of dictionaries
        return: list represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        args:
            ***dictionary: a double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = str(cls.__name__) + "json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
