#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_list = list(set(my_list))
    sum = 0
    for i in range(len(set_list)):
        sum += set_list[i]
    return sum
