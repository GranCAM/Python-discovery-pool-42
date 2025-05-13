#!/usr/bin/env python3

while (True):
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = num1 * num2
        print(" %i x %i = %i" %(num1, num2, num3))
        if (num3 > 0):
            print("This number is positive")
        else:
            if (num3 == 0):
                print("This number is both positive and negative")
            else:
                print("This number is negative")
        break
    except ValueError:
        print("That's not an number!")

