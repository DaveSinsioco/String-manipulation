# capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# ask the user to enter a string
string = input("Enter a string: ")

# create an empty string to store the result
result = ""

# make the first letter of the string, capital letter
result += string[0].upper()

# make all other letters in the string, small case
result += string[1:].lower()

# print the result
print(result)