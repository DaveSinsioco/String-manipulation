# swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# ask the user to enter a string
string = input("Enter a string: ")

# create an empty string to store the result
result = ""

# check then change every character in the string
for char in string:

    # check if the character is uppercase, convert it to lowercase if it is
    if char.isupper():
        result += char.lower()
        
    # check if the character is lowercase, convert it to uppercase if it is
    else:
        result += char.upper()

# print the result
print(result)        