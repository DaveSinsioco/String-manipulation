# Create a program that ask the user to input a complete statement. Print the number of words in the input.

# ask the user to input a complete statement
statement = input("Enter a complete statement: ")

# split the statement into words using space as a delimiter
words = statement.split()

# print the counted number of words
print(len(words))