#!/usr/bin/python3
def magic_calculation(a, b):
    final = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception("Too far")
            else:
                final += (a**b)/x
        except:
            final = b + a
            break
    return final

