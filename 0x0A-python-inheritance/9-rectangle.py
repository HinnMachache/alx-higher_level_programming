#!/usr/bin/python3
# 9-rectangle.py
"""Define a Geometry class that inherits BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Child Class inhertting from BaseClass Geometry"""
    def __init__(self, width, height):
        """Constructs a new class
        Arguments:
                width: Width f rectangle
                height: Height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates area of rectangle"""
        return self.__width * self.__width

    def __str__(self):
        """Return str() and print() representation of A Rectangle"""
        string = "[" + str((self.__class__.name)) + "] "
        string += str(self.__width) "/" + str(self.__height)
        return string
