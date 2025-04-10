# zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# asks user to input string and desired length
string = input("Enter a string: ")
length = int(input("Enter the desired length: "))

# prints the zeros multiplied by the difference between length and len(string) and adds the string
print("0" * (length - len(string)) + string)