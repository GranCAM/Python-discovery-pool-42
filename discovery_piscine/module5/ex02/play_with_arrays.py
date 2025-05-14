#! /usr/bin/env python3

arr = [1,9,2,4,3,7,4,5,6,9]
arr2 = []
i = 0
l = lambda n : n + 2
while (i < (len(arr))):
    if (arr[i] > 5):
        arr2.append(l(arr[i]))
    i += 1
print(f"{arr}")
print(f"{arr2}")