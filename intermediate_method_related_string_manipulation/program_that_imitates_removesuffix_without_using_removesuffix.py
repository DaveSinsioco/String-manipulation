# removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# ask the user to input the suffix to remove
suffix = input("Enter the suffix to remove: ")

# ask the user to input the string to remove the suffix from
string = input("Enter the string: ")

# check if the string starts with the suffix
if string.endswith(suffix):

    # remove the suffix from the string by letting the end removed.
    string = string[:-len(suffix)]
