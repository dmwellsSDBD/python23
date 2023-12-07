"""
File: wedBellRinger.py
Inputs the user's name and age, calculates how old the individual is, and outputs a sentence that contains each piece of information.
"""

name = input("Enter your name: ")
years = int(input("Enter your age: "))
curYear = 2023
birthYear = curYear - years
print(name, "is", years, "years old.", name, "was born in", birthYear, ".")
