#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        newList = my_string[:]
        for i in newList:
            if i == 'c' or i == 'C':
                newList.pop(i)
            else:
                return newList
