#!/usr/bin/python3

import sys

def downcase_it(inp):
    inp = inp.lower()
    return inp

c = sys.argv[1:]
i = 0
if len(sys.argv) > 1:
    while i < len(c):
        print(downcase_it(c[i]))
        i += 1
else:
    print("none")