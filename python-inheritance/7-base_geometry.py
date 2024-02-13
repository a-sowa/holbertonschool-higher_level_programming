#!/usr/bin/python3
"""
    Class named BaseGeometry
"""


class BaseGeometry:
    """Class named BaseGeometry """
    def __init__(self):
        """ empty init function """
        pass
    
    def area(self):
        """ Raises an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Checks type and value of given integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
