# rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# ask user to enter a string
string = input("Enter a string: ")

# starts a while loop to check if the first character is a space
while string.endswith(" "):
