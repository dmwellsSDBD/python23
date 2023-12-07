"""
Name: David Wells
File: fruitStore.py

Show a list of items
Have the user select an item
Put item in cart
Have the user enter how many of that item
Put quantity of item in cart
Allow user to add a second item
Put item in cart
Have the user enter how many of that item
Put quantity of item in cart
Limit cart to 3 items
Calculate and print price
Calculate and print tax
Add tax to price
Print final total
"""
print()
print()
print("Welcome to the Fruit Store")
print("__________________________")
print()
print("Select what you would like: ")
print("   1. Apples - $4.99")
print("   2. Bananas - $3.50")
print("   3. Oranges - $5.99")
print()
cart = 0

item1 = float(input("Enter the number of the first item you would like. If you are done shopping, Enter 0: "))

if item1 == 1:
   item = 4.99
elif item1 == 2:
   item = 3.50
elif item1 == 3:
   item = 5.99
else:
   item = 0

qty1 = int(input("How many of this item do you want: "))
cost1 = item * qty1
print("$", cost1) 

item2 = float(input("Enter the number of the second item you would like. If you are done shopping, Enter 0: "))

if item2 == 1:
   item = 4.99
elif item2 == 2:
   item = 3.50
elif item2 == 3:
   item = 5.99
else:
   item = 0

qty2 = int(input("How many of this item do you want: "))
cost2 = item * qty2
print("$", cost2)

cart = cost1 + cost2
print("You currently have $", cart, " in your cart.")

tax = cart * .08
cart = tax + cart

print("Your overall total is $", cart, " in your cart."
)


print()
