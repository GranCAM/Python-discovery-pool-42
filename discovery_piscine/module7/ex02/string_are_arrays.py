#! /usr/bin/env python3

import sys

if (len(sys.argv) != 2):
    print("none")
else:
    cad = sys.argv[1]
    i = 0
    n = 0
    while i < len(cad):
        if cad[i] == "z":
            print("z", end="")
            n += 1
        i += 1
    if n == 0:
        print("none")