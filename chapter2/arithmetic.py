print("Using Arithmetic in Python")
print("--------------------------")

a = 10
b = 25
c = 6

print("Value of a:", a, "value of b:", b,"Value of C:", c)

print("Arithmetic with Variables")
print("=========================")
print(a + b, a - b, a * b, a / b)

print(b / c, b % c, b ** c)

print(3 * a + b - (c // 2), "equals 52")
print(2 * c ** 2 + c + 2, "equals 80")
print("\n\n\n\n")
	
print("Division and Remainder")
print("======================\n\n")
print("Given 125 people at a dinner, and 8 seats per table...")
people = 125
tableSeats = 8
tablesNeededFloat = people / tableSeats
tablesNeededInt =  people // tableSeats
peopleLeftOut = people % tableSeats

print("\n\nDecimal tables needed is", tablesNeededFloat)
print("Integer tables needed is", tablesNeededInt)
print("People without a table", peopleLeftOut)

print("\n\nSplitting", 358, "by digit", 358 // 10, 358 % 10)

print("\n\n\nMixed-Mode Arithmetic")
print("++++++++++++++++++++++")
print("\n")
radius = input("Enter the radius: ")

circumfrance = float(radius) ** 2 * 3.14
print("The circumfrance is: ", circumfrance)

print(int(6.75)) # 6
print(round(6.75)) # 7  



