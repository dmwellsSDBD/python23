"""
File: binarytodecimal.py
Converts a string of bits to a decimal integer.
"""
bitstring = input("Enter a string of bits: ")
decimal = 0
exponent = len(bitstring) - 1 # subtract 1 - Off-By-One Error
for digit in bitstring:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent -= 1
print("The integer value is", decimal)