# slicing - An poperation that returns an subsection of a linear collection, for example: a sublist or a substring

name = "myfile.txt"
print(name[0:]) # prints entire string
print(name[:len(name)])

print(name[0:1]) # prints first character only
print(name[0:2]) # print first 2 characters

print(name[-3:]) # print last 3 characters
print(name[2:6]) # print characters starting at 2 ending 6

# Slicing structure
# <string>[<start index>:<end index>:<step size>]
sl = "abracadabra"
print(sl[4:7]) #cad
print(sl[:4]) #abra
print(sl[7:]) #abra
print(sl[::3])
print(sl[2::2]) #r c d b a
print(sl[::-2]) #a b d c r a
print(sl[::-1])