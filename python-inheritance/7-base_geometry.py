#!/usr/bin/python3
"""
    Class named BaseGeometry
"""


class BaseGeometry:
    """Class named BaseGeometry """
    def area(self):
        """ Raises an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Checks type and value of given integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.__value = value
