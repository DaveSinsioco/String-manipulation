# Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

# ask the user to input their name
name = input("Enter your full name: ")

# prints the name in pascal case using title() and Replace() methods
print(name.title().replace(" ", ""))