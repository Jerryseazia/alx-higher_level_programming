#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        value = []
        for x in my_list:
            if x % 2 is 0:
                value.append(True)
            else:
                value.append(False)
        return (value)

