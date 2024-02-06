#!/usr/bin/python3
"""
    Class that defines a square, its size, area and position then prints it
"""


class Square:
    """
    Function that creates an instance of Square with defined size
    using type and value verification
    """
    def __init__(self, size=0, position=(0, 0)):
        """
            Function that creates an instance of Square
            with defined size and position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Getter function that retrieves the square's size """
        return self.__size

    @property
    def position(self):
        """ Getter function that retrieves the square's position """
        return self.__position

    @size.setter
    def size(self, value):
        """ Setter function that set and checks type and value of given size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
            Setter function that set and checks type and value
            of given position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(
            isinstance(element, int) and element > 0
            for element in value
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Function that returns square's area """
        return self.__size * self.__size

    def my_print(self):
        """
            Function that prints a square in stdout with character '#'
            based on its size and position
        """
        if self.__size == 0:
            print()
        else:
            for idx_1 in range(self.__position[1]):
                print()
            for idx_2 in range(self.__size):
                for idx_3 in range(self.position[0]):
                    print("_", end='')
                for idx_4 in range(self.__size):
                    print("#", end='')
                print()
