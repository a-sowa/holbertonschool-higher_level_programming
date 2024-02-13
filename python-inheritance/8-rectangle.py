#!/usr/bin/python3
"""
    Class that defines a rectangle, its width and height.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that defines a rectangle, its width and height. """
    def __init__(self, width, height):
        """
            Creates an instance of Rectangle and checks for width
            and height type and value
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
