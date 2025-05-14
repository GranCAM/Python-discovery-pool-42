#! /usr/bin/env python3

arr = [1,2,3,4,5,6]
arr2 = []
i = 0
l = lambda n : n + 2
while (i < (len(arr))):
    arr2.append(l(arr[i]))
    i += 1
print(f"Original array: {arr}")
print(f"New array: {arr2}")