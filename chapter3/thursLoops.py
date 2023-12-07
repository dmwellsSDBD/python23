print("Traversing the Contents of a Data Sequence")
print("==========================================")

lst = list(range(4))
print(lst)

lst2 = list(range(1, 5))
print(lst2)


print("\n\nTraversing a Data Set")
# for <variable> in <sequence>:
#      <do something with variable>

for number in [6, 4, 8]: # Traverse a List
    print(number, end="\n")
    
for character in "Hi there!": # Traverse a String
    print(character, end="\n")
    
print("\n\nExamples of Traversing Data:")


for x in ['bat', 'hat', 'rat']: # Traverse a list of strings
    print(x) # Prints each string to a line
    
sum = 0 
for z in (6, 1, 2, 9, 3): # Traverse set of numberxs
    print(sum)
    sum = sum + z

print(sum)

print("\n\n")
for c in "rocket":  # Traverse characters in a string
    print(c)
    print(c.upper())
    

print("\n\n\n")
print("Specifying the Steps in a Range")
print("-------------------------------")

lst1 = list(range(1,6,1))
#              start at 1, go to 6 - 1, step 1
print("lst1: ", lst1)

lst2 = list(range(1,10,2))
print("lst2 by 2s: ", lst2)

lst3 = list(range(1,100,5))
print("lst3 by 5s: ", lst3)

theSum = 0
for count in range(2, 11, 2):
    theSum += count
    print("theSum: ", theSum)
    
print("Final Answer: ", theSum)

print("\n\nPractice the range() Function")
print("==============================")

r1 =  range(4)  # range(0,4)
print(r1, list(r1))
for i in r1:
    print(i)
    
r2 = range(10,20)
print(type(r2))
print(list(r2))

for x in range(2, 24, 2):
    print(x)
    
print("\n\nLoops that Count Down:\n")
for count in range(10, 0, -1):
    print(count, end=" ")
    
s = list(range(10, 0, -1))
print(s)
