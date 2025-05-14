#! /usr/bin/env python3

import sys

if (len(sys.argv) < 2):
    print("none")
else:
    args = sys.argv
    i = len(args) - 1
    while (i > 0):
        print(args[i])
        i -= 1