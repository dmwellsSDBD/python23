print('Question 1:')
# Get the 5th character in the string
text = "Hello, Python!"
#       01234567890123  Off-by-one
fifth = text[4] # line 1
print(fifth) # line 2

print("\n\nQuestion 2:")
# Print each character in the string one line at a time
text = "Python"
for char in text: # for loop
    print(char)# Code inside the for loop

print("\n\nQuestion 3:")
# Extract 'Merry' and print to console
text = "We wish you a Merry Christmas!"
#       012345678901234567890123456789
merry = text[14:19]# line that extracts the word ‘Merry’
print(merry) # print the word ‘Merry’ to the screen

print("\n\nQuestion 4:")
#extract the word Python from the string
text = "Learning Python is fun!"
#       01234567890123456789012
pyText = text[9:15] # Extract the word Python
print(pyText) # Print ‘Python’ to the string

print("\n\nQuestion 5:")
#write the text string in the opposite order then print it to the screen
text = "Reverse"
#            -1
revText = text[::-1] # Slice the string in reverse order
print(revText) # Print the reversed string to the screen

print("\n\n#4 in the Homework")
# Assume that the variable myString refers to a string, and the variable reversedString refers to an empty string. Write a loop that adds the characters from myString to reversedString in reverse order.
myString = "Welcome back Mason!"
reversedString = ""
# x = -1

for char in myString:
    reversedString = char + reversedString
#     char = myString[x]
#     reversedString += char
#     x -= 1
print(reversedString)

print("\n\nQuestion 6")
#Using the list below, write a for loop that will print only the names that start with the letter ‘C’. Each name should print on its own line.

heyLookAList = ['Eligha', 'Cody', 'Cooper', 'Carsten', 'Shaiden', 'James', 'Ethan', 'Mason', 'Corbin', 'Deven', 'Dylan', 'Lucas', 'Tobi', 'Trent']
# Create your code below:
for name in heyLookAList:
    if chr(67) in name[0]:
        print(name)
        
print("\n\nAnother Example:")




# List of 20 words
words = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Icicle", "Jackfruit", "Kiwi", "Lemon", "Mango", "Nectarine", "Orange", "Papaya", "Quince", "Raspberry", "Strawberry", "Tomato", "Cucumber", "Carrot", "caper"]
wordsWithC = []

for word in words:
    if word.startswith("C"):
        wordsWithC.append(word)
        
print(wordsWithC)