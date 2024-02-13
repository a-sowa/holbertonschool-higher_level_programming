#!/usr/bin/python3
"""
    Function that checks if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
        Returns True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False.
    """
    return any(issubclass(type(obj), subclass)
               for subclass in a_class.__subclasses__())
