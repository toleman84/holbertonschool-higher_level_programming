#!/usr/bin/python3
def fizzbuzz():
    for number in range(101):
        print(number)
        if number % 3:
            print("Fizz", end="")
        elif number % 5:
            print("Buzz", end="")
        elif number % 15:
            print("FizzBuzz", end="")
