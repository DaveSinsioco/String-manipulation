# rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

# ask the user for a string and a character to search
string = input("Enter a string: ")
char = input("Enter a character to search: ")

# find the placement of the string from the last character
placement = (string.rfind(char))

# print the result after checking if the character is not found in the string
if placement == -1:
    print(f"Value Error")
else:
    print(placement)