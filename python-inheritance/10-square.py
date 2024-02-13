#!/usr/bin/python3
"""
    Class that defines a square and its size.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square, inheriting from Rectangle."""
    def __init__(self, size):
        """Initialize a square with a given size."""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
