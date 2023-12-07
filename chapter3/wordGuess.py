"""
Author: David Wells
Date: 11/13/2023

Write a program called wordGuess.py. In the program you will List a selection of 10 words. Have the user guess what word you are \"thinking\". Write a while True statement that will loop through a series of code to enter user guess and either end the program or repeat the loop and ask again. When they guess the word the game ends.
"""
import random

# List of words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Randomly select a word from the list
secret_word = random.choice(words)

print("Guess the word! Here are your options:")
print(words)

while True:
    # Ask the user to guess
    user_guess = input("Enter your guess: ").lower()

    # Check if the guess is correct
    if user_guess == secret_word:
        print("Congratulations! You guessed the correct word.")
        break
    else:
        print("Wrong guess. Try again!")

print("Game Over.")