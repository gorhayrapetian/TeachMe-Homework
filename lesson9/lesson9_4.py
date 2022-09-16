# Write a function that checks if a given number is Palindrome or not.
# A palindrome is a word, number, phrase, or other sequence of characters which reads the
# same backward as forward, such as madam or racecar

def func(userResponse):
    return userResponse == userResponse[::-1]

userResponse = str(input('Enter a word: '))

Palindrome = func(userResponse)

if Palindrome:
    print(userResponse, 'is palindrome: ')
else:
    print(userResponse, 'is not palindrome: ')
