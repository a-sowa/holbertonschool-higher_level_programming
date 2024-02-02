#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0
    try:
        for i in range(x):
            value = my_list[i]
            if type(value) is int:
                print("{:d}".format(value), end="")
                integers_printed += 1
    except TypeError:
        pass
    print()
    return integers_printed
