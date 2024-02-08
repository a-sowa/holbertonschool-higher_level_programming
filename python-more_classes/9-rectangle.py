#!/usr/bin/python3
"""
    Class that defines a rectangle, its width, height,
    area and perimeter and prints it
"""


class Rectangle:
    """
        Class that defines a rectangle, its width, height, area and perimeter
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Function that creates an instance of Rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter function that retrieves the rectangle's width """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter function that set and checks type and value of given width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter function that retrieves the rectangle's height """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter function that set and checks type and value of given height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Function that returns rectangle's area """
        return self.width * self.height

    def perimeter(self):
        """ Function that returns rectangle's perimeter """
        return 2 * (self.width + self.height) if self.width != 0 and self.height != 0 else 0

    def __str__(self):
        """
            Function that returns a printable representation of rectangle
            with character '#' based on its height and width
        """
        symbol = Rectangle.print_symbol
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join([str(symbol) * self.width] * self.height)

    def __repr__(self):
        """  Function that returns a string representation of rectangle """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
            Prints a message when deleting an instance and
            decrements instances counter
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the Rectangle with the greater area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Return a new Rectangle with width and height equal to size """
        return cls(size, size)
