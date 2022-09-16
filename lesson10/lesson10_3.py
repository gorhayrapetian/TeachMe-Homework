# Write a Python program to check whether a given string is number or
# not using Lambda.

userResponse = input('Enter a number: ')

result = lambda x: x.isdigit()

print(result(userResponse))