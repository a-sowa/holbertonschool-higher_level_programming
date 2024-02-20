#!/usr/bin/python3
"""
    This file contains the definition of the Base class, which serves
    as the foundation for other classes in the project.
"""


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
