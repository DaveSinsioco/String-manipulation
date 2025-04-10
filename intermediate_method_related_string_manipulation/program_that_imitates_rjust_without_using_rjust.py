# rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# asks the user to enter a string and length
string = input("Enter a string: ")
length = int(input("Enter the length of the string needed: "))

# prints the string with spaces at the start to complete the length
print(" " * (length - len(string)) + string)