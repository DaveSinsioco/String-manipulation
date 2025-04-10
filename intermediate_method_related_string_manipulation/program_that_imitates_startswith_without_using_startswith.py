# startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# ask user to enter a string
string = input("Enter a string: ")

# ask user to enter a prefix
prefix = input("Enter a prefix: ")

# check if the string start with the prefix
if string.lfind(prefix) == 0:
    print(f"The string '{string}' start with the prefix '{prefix}'.")
else:
    print(f"The string '{string}' does not start with the prefix '{prefix}'.")    