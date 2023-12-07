sentence = "I went to work on Sunday"
ipAddress = "145.212.38.185"

# Methods that create a new string
print(sentence.lower())
print(sentence.upper())
print("    Space     ".strip())

# split makes a list of strings
words = sentence.split()
print(words)
ipParts = ipAddress.split('.')
print(ipParts)

print("*".join(words))
# print(words.replace('*', ' '))
print("Count of o: ", sentence.count('o'))

print(ipAddress.find('38'))

print(sentence[2:6].isalpha(), ipAddress[:3].isdigit())