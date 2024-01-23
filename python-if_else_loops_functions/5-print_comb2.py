#!/usr/bin/python3
for number in range(100):
    if number < 10:
        print(f"0{number},", end=' ')
    elif number < 99:
        print(f"{number},", end=' ')
    else:
        print(number)
