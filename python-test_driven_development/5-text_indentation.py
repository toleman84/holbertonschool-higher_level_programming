#!/usr/bin/python3
"""
4. Text indentation
"""


def text_indentation(text):
    """ prints a text with 2 new lines after each '. ? :' """
    if isinstance(text, str) is not True:
        raise TypeError('text must be a string')

    for char in '.?:':
        text = text.replace(char, char + '\n\n')
    revised = '\n'.join([lines.strip(' ') for lines in text.split('\n')])
    print(revised, end='')
