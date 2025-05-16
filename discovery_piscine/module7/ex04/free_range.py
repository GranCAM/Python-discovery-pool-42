#! /usr/bin/env python3

import sys

if (len(sys.argv) != 3):
    print("none")
else:
    l = []
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    if arg2 > arg1:
        for i in range(arg1, arg2):
            l.append(i)
        l.append(arg2)
    else:
        for i in range(arg2, arg1):
            l.append(i)
        l.append(arg1)
    print (l)