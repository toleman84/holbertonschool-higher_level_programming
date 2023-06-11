#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in a_dictionary:
        sorted_dictionary = sorted(a_dictionary.items(), key=lambda x:x[1])
    print(sorted_dictionary)
