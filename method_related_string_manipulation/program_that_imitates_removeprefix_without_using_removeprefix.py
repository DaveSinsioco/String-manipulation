# removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# ask the user to input the prefix to remove
prefix = input("Enter the prefix to remove: ")

# ask the user to input the string to remove the prefix from
string = input("Enter the string: ")

# check if the string starts with the prefix
if string.startswith(prefix):

    # remove the prefix from the string by letting the receding remain since length of prefix is the number of charactera to start from.
    
    string = string[len(prefix):]

print(string)
