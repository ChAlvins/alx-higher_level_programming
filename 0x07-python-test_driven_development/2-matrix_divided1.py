#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")