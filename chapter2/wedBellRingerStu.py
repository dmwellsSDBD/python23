"""
Name: <Enter your name>
File: wedBellRingerStu.py
Inputs the user's name and age, calculates how old the individual is, and outputs a sentence that contains each piece of information.
"""
name = input("Enter your name: ")
age = int(input("How old are you: "))
year = 2023
birYr = year - age
print("Hello", name, ". So you are", age, " years old, and were born in the year", birYr, ". Thank you for filling out our form", name, ".")
