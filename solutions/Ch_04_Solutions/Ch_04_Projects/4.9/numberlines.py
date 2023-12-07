"""
File: numberlines.py
Project 4.9

Copies the text from a given input file to a given
output file, numbering them as it goes.
"""

# Take the inputs
inName = input("Enter the input file name: ")
outName = input("Enter the output file name: ")

# Open the files
inputFile = open(inName, 'r')
outputFile = open(outName, 'w')

# Output the numbered lines
lineNumber = 0
for line in inputFile:
    lineNumber += 1
    outputFile.write("%4d> %s" % (lineNumber, line))
outputFile.close()
