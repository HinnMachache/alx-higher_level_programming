#!/usr/bin/python3
#2-matrix_divided.py
"""matrix_divided:
matrix (list of int or float),
div (int or float)
Returns:
    a new matrix
"""


def matrix_divided(matrix, div):
    """ A function that divides every
    element of a matrix by div
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if (not all(isinstance(row, list) and
                all(isinstance(num, (int, float)) for num in row)
                for row in matrix)):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError(
            "Each row of the matrix must have the same size")

    divided_matrix = []
    for row in matrix:
        divided_row = [round(element / div, 2) for element in row]
        divided_matrix.append(divided_row)

    return divided_matrix
