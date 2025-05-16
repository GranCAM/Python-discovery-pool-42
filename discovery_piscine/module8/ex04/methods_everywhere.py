#!/usr/bin/python3

import sys

def enlarge(inp):
    i = len(inp)
    while i < 8:
        inp = inp + "z"
        i += 1
    print(inp)

def shrink(inp):
    print(inp[0:8])

if len(sys.argv) < 2:
    print("none")
else:
    args = sys.argv[1:]
    for i in args:
        if len(i) > 8:
            shrink(i)
        elif (len(i) == 0):
            print(i)
        else:
            enlarge(i)