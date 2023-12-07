theSum = 0.0
data = input("Enter a number or just enter to quit: ") # loop control variable
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter a number or just enter to quit: ")

print("The sum is: ", theSum)


print("\n\nCount Controlled Loop")

# Summation with a for Loop
theSum = 0
for count in range(1, 100001):
    theSum += count
print("for Loop count: ", theSum)

# Summation with a while Loop
theSum = 0
count = 1
while count <= 100000:
    theSum += count
    count += 1
print("\n\nThe while Loop count Sum is: ", theSum)


# Counting down with a for Loop
for count in range(10, 0, -1):
    print("Counting down with for Loop:", count, end="\n")
    
# Counting down with a while Loop
count = 10
while count >= 1:
    print("Counting down with while Loop:", count, end="\n")
    count -= 1


# The break Statement
print("\n\nUsing the break Statement with while True loops")
theSum = 0.0
while True: # The loop will remain True until you tell it otherwise
    data = input("Enter a number or just enter to quit: ")
    if data == "":
        break
    number = float(data)
    theSum += number
print("The sum using a while True with break State is: ", theSum)

print("\n\nwhile True example 2:")
while True:
    number = int(input("Enter a numeric grade: "))
    if number >= 0 and number <= 100:
        break
    else:
        print("Error: grade must be between 100 and 0")
print("Student's grade is", number)        

print("\n\nwhile True Example 3: ")
done = False
while not done:
    number = int(input("Enter a numeric grade:" ))
    if number >= 0 and number <= 100:
        done = True
    else: 
        print("Error: grade must be between 100 and 0")
print("Student's grade is:", number)

