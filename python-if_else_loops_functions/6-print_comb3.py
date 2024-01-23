#!/usr/bin/python3
for digitOne in range(10):
    for digitTwo in range(digitOne + 1, 10):
        if digitOne == 8 and digitTwo == 9:
            print('{:02d}'.format(digitOne * 10 + digitTwo))
        else:
            print('{:02d}, '.format(digitOne * 10 + digitTwo), end='')
