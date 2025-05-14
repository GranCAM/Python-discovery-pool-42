#! /usr/bin/env python3

import sys

if (len(sys.argv) == 1):
    print("none")
else:
    args = sys.argv[1:]
    print(f"Parameters: {len(args)}")
    i = 0
    while i < len(args):
        print("%s: %d" %(args[i], len(args[i])))
        i += 1