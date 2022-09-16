#Write a Python function to get a string made of its first three characters of a specified string. If
#the length of the string is less than 3 then return the original string.

def func(word):
    userResponse = word[0:]
    return userResponse

userResponse = input("Write a word: ")

if len(userResponse) < 4:
    print(func(userResponse))

elif len(userResponse) > 3:
    print(userResponse[0:3])