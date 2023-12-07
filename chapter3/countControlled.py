print("Example 1:")
for x in range(4):
    print(x, end=" ")
    
print("\n\nExample 2:")
for cooper in range(50):
    print("Cooper", cooper, end="\n")
    
# print("\n\nExample 3:")
# for year in range(200000):
#     print(year, end="\n")
    
print("\n\nExample 4:")
print("------------")

product = 1 #Initializing variable product
for count in range(4):
    product = product * (count + 1)
    #print(product, end="\n")

print(product)

print("\n\nExample 5:")
print("----------------------------")
print("Using explicit 'lower bound':")

product = 1
for count in range(1, 5):
    product = product * count

print(product)

print("\n\nExample 6:")
print("---------------")
product = 1
for count in range(25, 50):
    print(count, end="\n")
    
# Explicit Count-Controlled for Loop
# for <variable> in range(<lower bound>, <upper bound +1):
#     <loop body>