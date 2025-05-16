#! /usr/bin/env python3

import sys

if (len(sys.argv) != 2):
    print("none")
else:
    args = sys.argv[1]
    check = input("What was the parameter? ").strip()
    if check == args:
        print("Good job!")
    else:
        print("Nope, sorry...")