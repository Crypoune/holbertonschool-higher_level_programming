#!/usr/bin/python3
"""This module provides a function that divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """Return a new matrix where each element is divided by div."""
    MATRIX_ERROR = "matrix must be a matrix (list of lists) of integers/floats"

    # Check matrix first
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) and row != [] for row in matrix)):
        raise TypeError(MATRIX_ERROR)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in (int, float):
                raise TypeError(MATRIX_ERROR)

    # Then check div
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
