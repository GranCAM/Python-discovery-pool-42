#!/usr/bin/python3

def greetings(inp = 'noble stranger'):
        try:
            float(inp)
            print("Error! It was not a name.")
        except ValueError:
            print(f"Hello, {inp}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
