#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_total = 0
    for i in range(len(sys.argv) - 1):
        sum_total += int(sys.argv[i + 1])
    print("{}".format(sum_total))
