#!/usr/bin/python3
"""
    Class that defines a rectangle, its width, height,
    area and perimeter and prints it
"""


class Rectangle:
    """
        Class that defines a rectangle, its width, height, area and perimeter
    """
    def __init__(self, width=0, height=0):
        """ Function that creates an instance of Rectangle """
        self.height = height
        self.width = width

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

    def area(self):
        """ Function that returns rectangle's area """
        return self.__height * self.__width

    def perimeter(self):
        """ Function that returns rectangle's perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ Function that returns a string representation of rectangle
            with character '#' based on its height and width
        """
        string_to_print = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string_to_print += '#'
            if i != self.__height - 1:
                string_to_print += '\n'
        return string_to_print
