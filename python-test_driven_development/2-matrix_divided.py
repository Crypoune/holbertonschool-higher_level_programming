#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int or float): The divisor.

    Returns:
        list of lists of float: a new matrix with all elements divided by div.

    Raises:
        TypeError:  If matrix is not a list of lists of numbers,
                    if rows are not of the same size,
                    or if div is not a number.
        ZeroDivisionError: If div is 0.
    """

    # Vérification que div est un nombre
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Vérification que div n'est pas zéro
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Vérification que matrix est une liste de listes
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification que chaque élément est un int ou float
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification que toutes les lignes ont la même taille
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Création de la nouvelle matrice divisée
    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
