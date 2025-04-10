# islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# ask user to enter a string
string = input("Enter a string: ")

# check if character is not lower case
for char in string:
    if ('A' <= char <= 'Z'):
        
        # if character has upper case characer, print the message and break the loop
        print("The string is not lower case.")
        break