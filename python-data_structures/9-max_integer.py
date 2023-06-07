#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    for x in my_list:
        if x > my_list[0]:
            return x
