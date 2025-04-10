# endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# ask user to enter a string
string = input("Enter a string: ")

# ask user to enter a suffix
suffix = input("Enter a suffix: ")

# check if the string ends with the suffix
if string.rfind(suffix) == len(string) - len(suffix):
    print(f"The string '{string}' ends with the suffix '{suffix}'.")
else:
    print(f"The string '{string}' does not end with the suffix '{suffix}'.")    