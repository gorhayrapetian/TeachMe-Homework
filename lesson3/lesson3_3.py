#Write a Python program to remove the n-th index character from a nonempty string.

userWord = input("Write the word you want to change: ")
userResponse = int(input("Write the index number of the letter which you want to remove: ")) 

print(userWord[:userResponse] + userWord[userResponse + 1:])