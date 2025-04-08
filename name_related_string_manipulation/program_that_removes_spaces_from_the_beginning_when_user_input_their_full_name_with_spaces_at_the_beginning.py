# Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

name = str(input("input full name: "))

# printing it using lstrip to remove spaces from the left

print(name.lstrip())