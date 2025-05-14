#! /usr/bin/env python3
while (True):
    try:
        age = int(input("Please tell me your age : "))
        print ("You are currently %d years old")
        print ("In 10 years, you'll be %d years old." %(age + 10))
        print ("In 20 years, you'll be %d years old." %(age + 20))
        print ("In 30 years, you'll be %d years old." %(age + 30))
        break
    except ValueError:
        print("POBRE PEPE QUE ESTO NO ES UNA EDAD")