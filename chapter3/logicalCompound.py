'''
Create a program to accept input of grade value to calculate averages

'''
print("Logical Example")
grade = int(input("Enter student grade: "))
if grade > 100:
    print("ERROR: grade must be between 100 and 0")
elif grade < 0:
    print("ERROR: grade must be between 100 and 0")
else: 
    print("There is code here to calculate averages.")
    print("Current grade is: ", grade)
    
print("\n\nCompound Logical Example")
grade = int(input("Enter student grade: "))
if grade > 100 or grade < 0:
    print("ERROR: grade must be between 100 and 0")
else:
    print("This is the else Statement. There is code here to calculate averages.")
    print("Current grade is: ", grade),
    
print("\n\nCompound Boolean Examples:")
A = True
B = False

andCond = A and B
print("A and B: ", andCond) # False

orCond = A or B
print("A or B: ", orCond) # True

notCond = not A
print("not A:", notCond) # False