print("Basic for Loop Structure")
print("------------------------")
for eachPass in range(4):
    print("It's alive!", end = " ")
    
print("\n\nfor Loop using Exponent")
print("---------------------------")

number = 2
exponent = 3
product = 1
for eachPass in range(exponent):
    product = product * number
    print(product, end = " ")

print(product) # print 8 because product was reset through the loop