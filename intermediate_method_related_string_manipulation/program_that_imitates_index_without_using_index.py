# index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

# ask the user for a string and a character to search
string = input("Enter a string: ")
char = input("Enter a character to search: ")

# initialize an empty list to store the indices
indeces = []

# iterate through the string and check if the character matches
for i in range(len(string)):
    if string[i] == char:
        indeces.append(i)

# print the first index, if not found print -1
if indeces:
    print(indeces[0])
else:
    print("-1")    