#!/usr/bin/python3
def element_at(my_list, idx):
    #If idx is negative, the function should return None
    if idx < 0:
        print("1")
        return None

    #If idx is out of range (> of number of element in my_list), the function should return None
    if idx > len(my_list):
        print("2")
        return None
    else:
        return my_list[idx]
