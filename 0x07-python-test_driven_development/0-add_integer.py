#!/usr/bin/python3
# 0-add_integer.py
"""add_integer:
a (int or float), b (int or float, optional Default is 98)
Returns:
    int: The sum of a and b as an integer.
"""


def add_integer(a, b=98):
    """Functions that adds a and B
    Returns sum integers as result
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a != a or b != b:
        raise TypeError("annot convert NaN to an intege")
    return (int(a) + int(b))
