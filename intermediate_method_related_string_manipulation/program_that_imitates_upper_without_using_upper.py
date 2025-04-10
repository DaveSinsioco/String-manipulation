# upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# asks the user to enter a string
string = input("Enter a string: ")

# prints the string in uppercase by making everything lowercase then swapcase
print(string.lower().swapcase())