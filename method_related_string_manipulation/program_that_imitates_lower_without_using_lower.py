# lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# ask user to enter a string
string = input("Enter a string: ")

# prints the string in lowercase by making everything uppercase then swapcase
print(string.upper().swapcase())