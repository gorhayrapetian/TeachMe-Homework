# Write a Python program to find if a given string starts with a given
# character using Lambda.

given_string = input('Enter a string: ')

given_character = input('Enter a character: ')

result = lambda x: x[0] == given_character

print(result(given_string))