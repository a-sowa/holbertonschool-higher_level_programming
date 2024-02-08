#!/usr/bin/python3
"""
    Class that defines a rectangle, its width and height
"""


class Rectangle:
    """ Class that defines a rectangle, its width and height """
    def __init__(self, width=0, height=0):
        """ Function that creates an instance of Rectangle """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """ Getter function that retrieves the rectangle's height """
        return self.__height

    @property
    def width(self):
        """ Getter function that retrieves the rectangle's width """
        return self.__width

    @height.setter
    def height(self, value):
        """
            Setter function that set and checks type and value of given height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """
            Setter function that set and checks type and value of given width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
