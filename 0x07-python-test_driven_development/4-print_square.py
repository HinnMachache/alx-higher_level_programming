#!/usr/bin/python3
#4-print_square.py
"""print_square : Prints square accordint to size
size must be of type integer, greater than 0

Args:
    size of square
"""


def print_square(size):
    """Function that prints square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is None:
        raise ValueError("Enter size")
    for i in range(size):
        for j in range(size-1):
            print("#")
        print("#")
