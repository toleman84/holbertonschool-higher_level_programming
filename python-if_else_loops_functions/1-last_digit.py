#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number %10
if last_digit > 5:
    print("Last digit of {} is {} greater than 5".format(number, last_digit))
elif last_digit == 0:
    print("the string and is 0")
elif last_digit < 6 and != 0:
    print("the string and is less than 6 and not 0")

# "Last digit of 5247 is 7 and is greater than 5"
