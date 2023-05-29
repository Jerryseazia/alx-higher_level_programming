#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    fx = 0
    while fx < x:
        try:
            print("{}".format(my_list[fx]), end="")
        except IndexError:
            break
        fx += 1
    print("")
    return fx
