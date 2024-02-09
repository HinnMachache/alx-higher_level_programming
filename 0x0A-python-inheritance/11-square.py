#!/usr/bin/python3
# 9-rectangle.py
"""Define a Geometry class that inherits BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Child Class inheriting from BaseClass Rectangle"""
    def __init__(self, size):
        """Child Class Subset"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
