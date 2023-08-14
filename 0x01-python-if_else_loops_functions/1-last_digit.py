#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absnumb = number if number > 0 else number * -1
print(f"Last digit of {number:d} is {absnumb % 10}", end=' ')
if absnumb % 10 > 5:
    print("and is greater than 5")
elif absnumb % 10 == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
