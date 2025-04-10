# center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# asks the user to enter a string and length
string = input("Enter a string: ")
length = int(input("Enter the length of the string needed: "))

# find the difference of length and string to find the spaces before and after string
diff = length - len(string)

# find the number of spaces before and after the string
spaces_before = diff // 2
spaces_after = diff - spaces_before

# print everything together
print(" " * spaces_before + string + " " * spaces_after)