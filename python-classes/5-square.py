#!/usr/bin/python3
"""
    Class that defines a square, its size and area then prints it
"""


class Square:
    """ Class that defines a square, its size and area then prints it """
    def __init__(self, size=0):
        """ Function that creates an instance of Square with defined size """
        self.__size = size

    @property
    def size(self):
        """ Getter function that retrieves the square's size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter function that set and checks type and value of given size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Function that returns square's area """
        return self.__size * self.__size

    def my_print(self):
        """
            Function that prints a square in stdout with character '#'
            based on its size
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print('')
