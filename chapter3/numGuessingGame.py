"""
Author: David Wells
Date: 11/13/2023
"""
import random

smaller = int(input("Enter your smaller number: ")) 
larger = int(input("Enter your larger number: "))

myNumber = random.randint(smaller, larger)
count = 0 

while True:
    count += 1
    userNumber = int(input("Enter your guess between the numbers of" + str(smaller) + " and " + str(larger) + ": "))
    if userNumber < myNumber:
        print("Your Guess is too small")
    elif userNumber > myNumber:
        print("Your guess is too large")
    else:
        print("Congratulations! You've got it in", count, "tries!")
        break