#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a
    tuple_b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b

    first_element = tuple_a[0] + tuple_b[0]
    second_element = tuple_a[1] + tuple_b[1]

    return (first_element, second_element)
