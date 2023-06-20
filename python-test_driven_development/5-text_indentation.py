#!/usr/bin/python3
"""
doc
for
module
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        dic = {'.': '.\n\n', '?': '?\n\n', ':': ':\n\n'}
        for k, v in dic.items():
            text = text.replace(k, v)
        print(text, end='')
