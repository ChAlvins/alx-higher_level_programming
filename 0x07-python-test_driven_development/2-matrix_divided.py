#!/usr/bin/python3
"""
A function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix
    Args:
        matrix: list of elements of integers/floats
        div: number which divides the matrix
    Returns:
        A new matrix with the result of the division
    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elements of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(matrix_msg)

    len_elem = 0
    msg_size = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(matrix_msg)

        if len_elem != 0 and len(elements) != len_elem:
            raise TypeError(msg_size)

        for num in elements:
            if not type(num) in (int, float):
                raise TypeError(matrix_msg)

        len_elem = len(elements)

    i = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (i)
