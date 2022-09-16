#Write a Python function to get a string made of 4 copies of the last two characters of a
#specified string (length must be at least 2).

def func(word):
    userResponse = word[-2:]
    return userResponse * 4

userResponse = input("Write something here: ")

if len(userResponse) < 2:
        print("Your word must include at least 2 letters. ")
elif len(userResponse) > 2:
    print(func(userResponse))