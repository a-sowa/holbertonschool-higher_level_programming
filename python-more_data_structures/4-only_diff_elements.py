#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    different_values_1 = set_1.difference(set_2)
    different_values_2 = set_2.difference(set_1)
    different_values_1.update(different_values_2)
    return different_values_1
