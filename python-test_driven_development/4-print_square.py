#!/usr/bin/python3
"""
    Module that prints a square with the character #
"""


def print_square(size):
    """ Checks is an int and > 0 and prints the square with given size """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/4-print_square.txt")
