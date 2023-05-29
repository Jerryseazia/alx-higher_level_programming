#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    show = 0
    for fx in range(x):
        try:
            print("{:d}".format(my_list[fx]), end="")
            show += 1
        except (TypeError, ValueError):
            continue
    print("")
    return show
