#! /usr/bin/env python3

import sys

if (len(sys.argv) == 1):
    print("none")
else:
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i].endswith("ism"):
            i += 1
        else:
            args[i] = args[i] + "ism"
            print(f"{args[i]}")
            i+= 1