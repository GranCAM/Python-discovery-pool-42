#! /usr/bin/env python3

while (True):
    try:
        num = int(input("Enter a number less than 25 \n"))
        if (num > 24):
            print ("Error")
            break
        else:
            while (num < 26):
                print("Inside the loop, my variable is %d" %(num))
                num += 1
        break
    except ValueError:
        print("That's not an number!")
