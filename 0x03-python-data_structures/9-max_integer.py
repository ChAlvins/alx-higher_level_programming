#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    biggest_int = my_list[0]
    for i in range(len(my_list)):
        if biggest_int < my_list[i]:
            biggest_int = my_list[i]
        else:
            continue
    return biggest_int
