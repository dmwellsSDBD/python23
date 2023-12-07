'''
In this example, you need to ask the user for the upper and lower bounds.

Initiate a variable called theSum
for Loop will have a variable called number
'''

# initiate variables

lower = int(input("Enter a lower bound: "))
upper = int(input("Enter a upper bound: "))

theSum = 0

# Create our for Loop
for number in range(lower, upper + 1):
    theSum = theSum + number
    print(theSum, end="\n")
    
print(theSum)