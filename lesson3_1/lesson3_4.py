# Write a Python program to change a given string to a new string where the first and last chars
#have been exchanged.

userResponse = input("Write a random word here: ")

# solution number 1
def func(UserResponse):
      return UserResponse[-1:] + UserResponse[1:-1] + UserResponse[:1]

print(func(userResponse))

# solution number 2 
print(userResponse[-1:] + userResponse[1:-1] + userResponse[:1])