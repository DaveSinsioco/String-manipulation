# Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.


# asks user to input number (0-1000)
number = (input("Input a number (0-1000): "))

# counts the digits of the number
digit_count = len(number)

# prints the zeros multiplied by the difference between 6 and the digit count and adds the number
print("0" * (6 - digit_count) + number)