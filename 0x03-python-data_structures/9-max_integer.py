#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        largest = my_list[0]
        for x in my_list:
            if x > largest:
                largest = x
        return (largest)
    else:
        return (None)
