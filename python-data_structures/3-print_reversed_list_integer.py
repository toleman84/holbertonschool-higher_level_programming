#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in my_list:
        i.reverse()
        #rev = i[::-1]
        print("{:d}".format(i))
