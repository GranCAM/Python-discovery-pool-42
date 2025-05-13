#! /usr/bin/env python3
while (True):
    try:
        num1 = int(input("Give me the first number: "))
        num2 = int(input("Give me the second number: "))
        print("Thank you!")
        print("%d + %d = %d" %(num1, num2, num1 + num2))
        print("%d - %d = %d" %(num1, num2, num1 - num2))
        print("%d / %d = %f" %(num1, num2, num1 / num2))
        print("%d * %d = %d" %(num1, num2, num1 * num2))
        break
    except ValueError:
        print("Not a number you dum dum")