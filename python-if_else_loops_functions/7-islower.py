#!/usr/bin/python3
def islower(c):
    for letter in c:
        if ord(letter) >= 97 and ord(letter) <= 122:
            return True
        else:
            return False
