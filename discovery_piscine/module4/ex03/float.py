#! /usr/bin/env python3
while (True):
   try:
      num = float(input ("Give me a number: "))
      if len(str(num)) > 11:
         print("MUUUY GRANDE")
         break
      if num.is_integer():
         print("The number is an integer")
      else :
         print("The number is a decimal")
      break
   except ValueError:
      print("Not a number you dum dum")