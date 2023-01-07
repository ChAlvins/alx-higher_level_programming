#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for i in element:
            print('{:d}'.format(i), end='')
            if i != element[-1]:
                print(' ', end='')
        print("")
