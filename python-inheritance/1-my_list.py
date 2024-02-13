#!/usr/bin/python3
"""
    A custom list class that inherits from the built-in list class.
"""


class MyList(list):
    def print_sorted(self):
        """ Prints the elements of the list in sorted order (ascending). """
        sorted_list = sorted(self)
        print(sorted_list)

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/1-my_list.txt")
