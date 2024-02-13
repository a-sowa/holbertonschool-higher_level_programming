#!/usr/bin/python3
"""
    Function that checks if an object is an instance of a class
    or an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
        Returns True if the object is an instance of, or if the object
        is an instanceof a class that inherited from, the specified class
        Otherwise returns False.
    """
    return isinstance(obj, a_class)
