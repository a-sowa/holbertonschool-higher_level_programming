#!/usr/bin/python3
"""
    This file contains the definition of the Base class, which serves
    as the foundation for other classes in the project.
"""

import json


class Base:
    """ Base class for managing unique identifiers. """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Constructor for the Base class.

            Parameters:
            - id: An optional integer identifier.
            If provided, it's assigned to the 'id' attribute.
            If not provided, increments __nb_objects and assigns
            the new value to 'id'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Convert a list of dictionaries to its JSON string representation.

            Parameters:
            - list_dictionaries: List of dictionaries.

            Returns:
            - JSON string representation of the list of dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Save the JSON string representation of list_objs to a file.

            Parameters:
            - cls: Class reference.
            - list_objs: List of instances inheriting from Base.

            Notes:
            - If list_objs is None, an empty list is saved.
            - The filename is generated based on the class name.
            - The file is overwritten if it already exists.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(json_str)
