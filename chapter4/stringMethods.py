# sentence = input("Enter a sentence: ")
# listOfWords = sentence.split()
# print("There are", len(listOfWords), "words.")
# print(listOfWords)

# sum = 0
# for word in listOfWords:
#     sum += len(word)
# print("The average word length is", sum/len(listOfWords))

# When using string methods, here is the format
# <an object>.<method name>(argument-1, ... , argument-n)


s = "There are currently 15 days left until Christmas break."
print(len(s))
print(s.center(55))
print(s.center(75))
print(s.center(60))

print("There are", s.count('r'), "letter 'r's in the sentence")

print(s.startswith("The"))
print(s.startswith("curren"))

print(s.find('Christmas'))

print("ABC".isalpha())
print("ABC".isdigit())

print("     Hello there!     ".strip())
s = "Hello there!"
print(s.upper())
print(s.lower())
print(s.strip('!'))

x = "botnet.exe"
print(x.split('.'))