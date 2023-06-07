#!/usr/bin/python3
def element_at(my_list, idx):
    #If idx is negative, the function should return None
    if idx < 0:
        return None
    #If idx is out of range (> of number of element in my_list), the function should return None
    print(format(len(my_list)))
    if idx > len(my_list):
        return None
    #Write a function that retrieves an element from a list.
    return my_list[idx]
