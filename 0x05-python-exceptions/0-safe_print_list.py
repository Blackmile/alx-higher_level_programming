#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    Sum = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            Sum += 1
        print()
    except:
        print()
        return Sum
    return Sum
