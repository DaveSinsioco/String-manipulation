# count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# asks the user for a string
string = input("Enter a string: ")

# asks the user for a subtext to count
char = input("Enter a subtext to count: ")

# initializes count, using for loop to check if i == char, add 1 to count
count = 0
for i in string:
    if i == char:
        count += 1
