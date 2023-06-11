#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = []
    for k, v in a_dictionary:
        if k:
            new_dict[k].append(key)
        if v:
            new_dict[v].append(value)
    print(new_dict)

#new_list.append(replace)