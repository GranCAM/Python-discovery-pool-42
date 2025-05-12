#!/usr/bin/env python3

while (True):
    try:
        num = int(input())
        if (num != 0):
            print("This number is different from zero")
        else:
            print("This number is equal to zero")
        break
    except ValueError:
        print("That's not an number!")
