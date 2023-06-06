#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for x in range(list_length):
        divide = 0
        try:
            divide = my_list_1[x] / my_list_2[x]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            new.append(divide)
    return new
