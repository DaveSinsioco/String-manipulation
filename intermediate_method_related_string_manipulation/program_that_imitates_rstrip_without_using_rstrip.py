# rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# ask user to enter a string
string = input("Enter a string: ")

# starts a while loop to check if the last character is a space
while string.endswith(" "):

    # if the last character is a space, remove it
    string = string[:-1]
