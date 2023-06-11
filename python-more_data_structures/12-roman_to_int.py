#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

    value = 0
    for i in range(len(roman_string)):
        if i > 0 and dict[roman_string[i]] > dict[roman_string[i - 1]]:
            value += dict[roman_string[i]] - 2 * dict[roman_string[i - 1]]
        else:
            value += dict[roman_string[i]]
    return value
