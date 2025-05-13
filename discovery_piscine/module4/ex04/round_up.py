#! /usr/bin/env python3
while (True):
   try:
      num = float(input ("Give me a number: "))
      print(math.ceil(num))
      break
   except ValueError:
      print("Not a number you dum dum")