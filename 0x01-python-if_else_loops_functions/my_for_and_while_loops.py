#!/usr/bin/python3
"""for then while loop"""


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in numbers:
    print(item)


i = 0
while i <= len(numbers):
    print(numbers[i])
    i += 1
