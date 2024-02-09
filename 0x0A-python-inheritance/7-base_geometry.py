#!/usr/bin/python3
# 7-base_geometry.py
"""integer_validator: Validate if a specified value
is an integer
"""


class BaseGeometry:
    """BaseGeometry Class"""
    def area(self):
        """Calculate Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if parameter is an integer.

        Args:
            name (str): Name of the parameter.
            value (int): Value of parameter.

        Returns:
            ValueError: if value <= 0
            TypeError: if valuie != int
        """
        if type(value) != int:
            raise TypeError("[TypeError] {} must be an integer".format(name))
        if value <= 0:
            raise ValueError("[ValueEror] {} must be greater than 0".format(name))
