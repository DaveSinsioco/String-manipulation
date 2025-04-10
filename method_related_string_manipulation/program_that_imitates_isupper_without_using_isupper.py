# isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# ask user to enter a string
string = input("Enter a string: ")

# check if character is not upper case
for char in string:
    if ('a' <= char <= 'z'):
        
        # if character has lower case characer, print the message and break the loop
        print("The string is not upper case.")
        break