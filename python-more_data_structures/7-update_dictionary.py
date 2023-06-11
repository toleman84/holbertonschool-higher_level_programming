#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = []
    for k in a_dictionary:
        new_dict[k].append(key)
        for v in a_dictionary:
            new_dict[v].append(value)
    print(new_dict)

#new_list.append(replace)