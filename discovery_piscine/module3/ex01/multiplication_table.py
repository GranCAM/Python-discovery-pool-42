#! /usr/bin/env python3

while (True):
    try:
        num = int(input("Enter a number \n"))
        iter = 0
        while (iter < 10):
            print ("%d x %d = %d" %(iter, num, num * iter))
            iter += 1
        break
    except ValueError:
        print("That's not an number!")
