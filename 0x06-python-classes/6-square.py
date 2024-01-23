#!/usr/bin/python3
"""
a class Square that defines a square by: (based on 1-square.py)
Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0a
"""
class Square:
    """ A  class Square that defines a square by: (based on 1-square.py)"""
    def __init__(self, size = 0):
         """
        Initialize a new Square with
        Private instance attribute: size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """get current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size the a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Public Object Instance for calculating area
        """
        area = self.__size * self.__size
        return (area)

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("")
            for j in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
