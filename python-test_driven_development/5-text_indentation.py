#!/usr/bin/python3
"""
    Module that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ Checks if text is a string and add a 2 lines aftes '.' '?' and ':' """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        print("\n\n", end="")

    char_list = [".", "?", ":"]
    new_line_added = False

    for char in text:
        if new_line_added and char == " ":
            continue
        print(char, end="")
        if char in char_list:
            print("\n\n", end="")
            new_line_added = True
        else:
            new_line_added = False


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/4-print_square.txt")
