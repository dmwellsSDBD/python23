print("\n\nExample 1:")
A = 2
B = 3
result = A + B * 2 < 10 or B == 2
# Multiply first B * 2:    A + 6 < 10 or B == 2
# Add next A + 6:  8 < 10 or B == 2
# Comparison 8 < 10 then B == 2:  True or False
# True
print(result)

print("\n\nExample 2:")
x = 40
y = 20
print(x == y or x == 2*y) # True
# x == y or x == 40
# 40 == 20 or 40 == 40
#  False or True
#     True
print(x > y and x > 2 * y) # False
# x > y and x > 40
# False and False
#     False
print(not(x == y or x == 2*y)) # False
# not(x == y or x == 40)
# not(False or True)
# not(True)
# False
print(y > x**2, not(x <= y * 2)) # False False
# 20 > 1600, not(40 <= 40)
# False, not(True)
# False False
# 30 != 30    not True == False
