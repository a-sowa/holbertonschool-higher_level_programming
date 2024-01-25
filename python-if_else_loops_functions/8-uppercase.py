#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        char = str[i]
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            char = chr(ord(str[i]) - 32)
        if i + 1 == len(str):
            print(f"{char}")
        else:
            print(f"{char}", end='')
