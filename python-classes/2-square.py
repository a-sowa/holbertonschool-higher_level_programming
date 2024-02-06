#!/usr/bin/python3
"""
Class that defines a square
"""


class Square:
    """
    Function that creates an instance of Square with defined size
    using type and value verification
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
