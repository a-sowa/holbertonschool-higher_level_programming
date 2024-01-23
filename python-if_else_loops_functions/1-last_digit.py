#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
text = f"Last digit of {number} is {lastDigit} and is"

if lastDigit > 5:
    print(f"{text} greater than 5")
elif lastDigit == 0:
    print(f"{text} 0")
else:
    print(f"{text} less than 6 and not 0")
