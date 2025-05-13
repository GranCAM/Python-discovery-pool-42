#! /usr/bin/env python3

while (True):
    num = 0
    iter = 0
    while (num < 11):
        print ("Table of %d: " %(num), end="")
        while (iter < 11):
            mult = num * iter
            print ("%d "%(mult), end="")
            iter += 1
        num += 1
        iter = 0
        print("")
    break
