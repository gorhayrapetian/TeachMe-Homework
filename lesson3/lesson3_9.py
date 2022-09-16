#Append new string in the middle of a given (even number of characters) string
#Example:

string = input("create a string: " )

new_string = input("create a new string: ")

if len(string) >= 7:
    print("you name must include 6 letters. ")
elif len(string) <=5:
    print("your name must be 6 letters: ")
else:
    print(string[0:3] + new_string + string[3:])

# solution 2

a = "python"

b = "new"

letters_number = (len(a))

print(a[:letters_number // 2] + b + a[letters_number // 2:])

print(letters_number)