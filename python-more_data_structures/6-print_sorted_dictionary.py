#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in a_dictionary:
        sorted_dictionary = sorted(i.items())
    print(sorted_dictionary, end="\n")
