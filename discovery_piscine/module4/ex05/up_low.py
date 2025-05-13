#! /usr/bin/env python3
string = input ()
i = 0
while (i < len(string)):
    if string[i].isupper():
        print(string[i].lower(), end="")
    else:
        print(string[i].upper(), end="")
    i += 1
print("")