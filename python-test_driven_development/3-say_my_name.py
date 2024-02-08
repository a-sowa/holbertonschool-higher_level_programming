#!/usr/bin/python3
"""
    Module that prints: My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
        Checks if first_name and last_name are strings
        Then prints: My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = f"My name is {first_name} {last_name}"
    print(full_name)


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
