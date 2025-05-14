#! /usr/bin/env python3

arr = [1,11,9,2,4,3,7,2,3,5,1,9999,4,5,6,9]
arr2 = []

i = 0
l = lambda n : n + 2
while (i < (len(arr))):
    if (arr[i] > 5):
        arr2.append(l(arr[i]))
    i += 1
i = 0
arr2 =list(dict.fromkeys(arr2))
print(f"{arr}")
print("{", end="")
while (i < (len(arr2) - 1)):
    print(arr2[i], end=", ")
    i += 1
print(arr2[len(arr2) - 1], end="")
print("}")
