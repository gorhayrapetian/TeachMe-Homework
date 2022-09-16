# Write a Python program to get a string made of the first 2 and the last 2 chars from a
#given string.

userResponse = str(input("Please, write your name here: "))
print(userResponse[0:2] + userResponse[-2:])