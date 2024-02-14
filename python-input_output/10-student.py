#!/usr/bin/python3
"""
A simple class representing a Student and a method
to convert its attributes to a JSON-like dictionary.
"""


class Student:
    """
    Represents a Student with first name, last name, and age attributes.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of strings specifying attribute
                                    names to be retrieved.
                                    If None, retrieve all attributes.

        Returns:
            dict: A dictionary representing the selected
            attributes of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
