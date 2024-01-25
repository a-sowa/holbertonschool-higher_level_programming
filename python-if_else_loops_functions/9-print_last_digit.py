#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        lastDigit = number % 10
    else:
        lastDigit = (number % -10) * -1
    print(lastDigit, end='')
    return lastDigit