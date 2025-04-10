# title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# asks user to enter a string
string = input("Enter a string: ")

# creates a variable to store the result
result = ""

# split the string into words, store it in result
result = string.split()

# use i to iterate through the words in the string, and capitalize the first letter of each word, connect it with "end"
for i in range(len(result)):
    print(result[i].capitalize(), end=" ")
