#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            ln = ord(i) - 32
        else:
            ln = ord(i)
        print("{:c}".format(ln), end="")
    print("")
