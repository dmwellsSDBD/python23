"""
File: newton.py
Project 6.4

Compute the square root of a number (uses recursive function with
default second argument).

1. The input is a number, or enter/return to halt the
   input process.

2. The outputs are the program's estimate of the square root
   using Newton's method of successive approximations, and
   Python's own estimate using math.sqrt.
"""

import math

# Initialize the tolerance
TOLERANCE = 0.000001

def newton(x, estimate = 1):
    """Returns the square root of x."""
    # Compute the difference and test for the base case
    if limitReached(x, estimate):
        return estimate
    else:
        # Recurse after improving the estimate
        return newton(x, improveEstimate(x, estimate))

def limitReached(x, estimate):
    """Returns True if the estimate is within
    the tolerance or False otherwise."""
    difference = abs(x - estimate ** 2)
    return difference <= TOLERANCE

def improveEstimate(x, estimate):
    """Returns an improved estimate."""
    return (estimate + x / estimate) / 2

def main():
    """Allows the user to obtain square roots."""
    while True:
        # Receive the input number from the user
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
             break
        x = float(x)
        # Output the result
        print("The program's estimate is", newton(x))
        print("Python's estimate is     ", math.sqrt(x))

if __name__ == "__main__":
    main()
