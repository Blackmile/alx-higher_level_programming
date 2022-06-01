#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -number
    n = number % 10
    number = -number
    n = -n
else:
    n = number % 10
if n > 5:
    print("last digit of", number, "is", n, "and is greater than 5")
elif n == 0:
    print("last digit of", number, "is", n, "and is 0")
else:
    print("last digit of", number, "is", n, "and is less than 6 and not 0")
