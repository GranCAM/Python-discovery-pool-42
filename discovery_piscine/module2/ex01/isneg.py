#!/usr/bin/env python3
while (True):
    try:
        num = int(input())
        if (num > 0):
            print("This number is positive")
        else:
            if (num == 0):
                print("This number is both positive and negative")
            else:
                print("This number is negative")
        break
    except ValueError:
        print("That's not an number!")