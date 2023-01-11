#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    x = 0
    y = 0
    for i in my_list:
        x += i[0] * i[1]
        y += i[1]
    return x / y
