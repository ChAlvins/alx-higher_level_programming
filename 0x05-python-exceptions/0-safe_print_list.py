#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    list_elements = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            list_elements += 1
        print()
    except IndexError:
        pass
        print()
    return list_elements
