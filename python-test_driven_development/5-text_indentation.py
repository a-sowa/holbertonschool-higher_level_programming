#!/usr/bin/python3
"""
    Module that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ Checks if text is a string and add a 2 lines aftes '.' '?' and ':' """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""

    for char in text:
        if char in ['.', '?', ':']:
            new_text += char + "\n\n"
        else:
            new_text += char

    print(new_text, end='')


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/4-print_square.txt")
