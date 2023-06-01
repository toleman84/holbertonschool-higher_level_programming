#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numbers = len(sys.argv)
    for number in range(1, numbers):
        sum += int(sys.argv[number])
    print("{}".format(sum))
