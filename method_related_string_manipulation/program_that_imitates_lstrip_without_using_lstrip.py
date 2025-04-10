# lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# ask user to enter a string
string = input("Enter a string: ")

# starts a while loop to check if the first character is a space
while string.startswith(" "):

    # if it is a space, the receding string will remain
    string = string[1:]

# print string
print(string)