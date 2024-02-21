#!/usr/bin/python3
"""
   This file contains the definition of the Rectangle class,
   which inherits from the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """ Rectangle class, inheriting from the Base class. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Constructor for the Rectangle class.

            Parameters:
            - width: Width of the rectangle.
            - height: Height of the rectangle.
            - x: X-coordinate of the rectangle.
            - y: Y-coordinate of the rectangle.
            - id: Optional identifier. If provided, passed to the Base class;
            otherwise, generated by Base.

            Public Attributes:
            - id: Unique identifier for the rectangle.
            - width: Width of the rectangle.
            - height: Height of the rectangle.
            - x: X-coordinate of the rectangle.
            - y: Y-coordinate of the rectangle.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """
            Print the Rectangle instance with the character '#'
            considering x and y coordinates.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
            Override the __str__ method to represent
            the Rectangle instance as a string.
        """
        str_1 = f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        str_2 = f" - {self.width}/{self.height}"
        return f"{str_1}{str_2}"

    def update(self, *args, **kwargs):
        """
            Update the Rectangle attributes using
            the provided arguments and key-worded arguments.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
