# x = 8
# y = 2
# z = 2

# print(x == y)
# print(y >= x)
# print(z != y)
# print(z != x)
# print(y == z)
import math

print("\n\nTwo-Way Selection : if-else Statment")
area = float(input("Enter the area: "))
if area > 0:
    radius = area/math.pi
    print("The radius is: ", radius)
else:
    print("Error: the area must be a positive number, you nit-wit.")
    
print("\n\nExample 2: Using input statements")
print("\n\n")

first = int(input("Enter a whole number: "))
second = int(input("Enter a second whole number: "))

if first > second:
    maximum = first
    minimum = second
else: 
    maximum = second
    minimum = first
    
#print("Maximum: ", maximum)             Both of these options work
#print("Minimum: ", minimum)
print("Maximum: ", max(first, second))
print("Minimum: ", min(first, second))

print("\n\nOne-Way Selection Statement")
age = 49
if age > 40:
    print("Damn, you are old!")

print("Your age is: ", age)

print("\n\n\nMulti-Way Selection Statement")
grade = int(input("Enter a numeric grade: "))
if grade > 89:
    letter = "A"
elif grade > 79:
    letter = "B"
elif grade > 69:
    letter = "C"
else:
    letter = "F"
    
print("The letter grade is: ", letter)

print("\n\nCompound Boolean Expressions:")
number = int(input("Enter a numeric grade: "))
# if number > 100:
#     print("Error: grade must be between 100 and 0")
# elif number < 0:
#     print("Error: grade must be between 100 and 0")
# else:
    #run code that is here
    
if number > 100 or number < 0:
    print("Error: grade must be between 100 and 0")
else:
    print("Good job poopin'!")
    
if number >= 0 and number <= 100:
    print("Good job poopin'!")
else:
    print("Error: grade must be between 100 and 0")