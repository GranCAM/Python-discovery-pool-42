#! /usr/bin/env python3

import sys

if (len(sys.argv) != 3):
    print("none")
else:
    args = sys.argv[1:]
    n = args[1].count(args[0])
    if n != 0:
        print(n)
    else:
        print("none")