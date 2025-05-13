#! /usr/bin/env python3

while (True):
    try:
        num = float(input("Enter a number \n"))
        iter = 0
        while (iter < 10):
            print (" %i x %i = %i" %(iter, num, num * iter))
            iter += 1
        break
    except ValueError:
        print("That's not an number!")
