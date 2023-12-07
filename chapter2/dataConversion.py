print("Converting Data Types")
print("#####################")
x = 35.2
y = 24

print("type() Function:")
print(type(x), type(y)) # float int
print(x, 'converts to integer', int(x))
print(y, 'converts to float', float(y))

print('\n\n\n')
resStr = str(x + y)
print(type(resStr))
print("The result of the resStr variable is" + resStr)

print("\n\n")
charList = list("abracadabra")

print(resStr, charList)
listStr = str(['a', 'c', 'e'])
print(type(listStr), listStr)

print("\n\n______________________________________")
ANum = ord('A')
BNum = ord('B')
ZNum = ord('Z')
spaceNum = ord(' ')
print("ANum: ", ANum, "BNum: ", BNum, "ZNum: ", ZNum, "spaceNum: ", spaceNum)
print("---------------------------------------\n\n")

print("Character Function")
print("------------------")
print("chr(100): ", chr(100), "chr(111): ", chr(111), "chr(103): ", chr(103))




