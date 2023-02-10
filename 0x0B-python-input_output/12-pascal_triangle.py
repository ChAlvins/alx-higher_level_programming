#!/usr/bin/python3
"""module with a function returns a list of lists of integers
representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    Creates a pascal triangle

    Attributes:
        n (int): The n exponent for triangle

    Return:
        A matrix with values for the triangle
    """
    pascal = []
    triangle = []

    for i in range(int(n)):
        new = pascal[:]
        new.append(1)
        pos = len(pascal)
        for i in range(1, pos):
            new[i] = pascal[i - 1] + pascal[i]
        pascal = new[:]
        triangle.append(pascal)
    return triangle
