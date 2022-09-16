#Append new string in the middle of a given (even number of characters) string
#Example:

userResponse = input("Write some words here: ")

def func(userResponse):
    length = len(userResponse)
    
    if length > 2:
        if userResponse[-3:] == 'ing':
            userResponse = userResponse + 'ly'
        else:
            userResponse = userResponse + 'ing'
    return userResponse

print(func(userResponse))