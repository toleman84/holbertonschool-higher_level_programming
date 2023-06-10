#!/usr/bin/python3
def search_replace(my_list, search, replace):
    #function that replaces all occurrences of an element by another in a new list.
    new_list = []
    
    if search <= len(my_list):
        new_list[search] = replace
        return new_list

    #my_list is the initial list
    #search is the element to replace in the list
    #eplace is the new element
