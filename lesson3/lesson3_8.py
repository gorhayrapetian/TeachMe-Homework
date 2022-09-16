#Create a string made of the first, middle and last character of given string with odd number of
#symbols

userResponse = str(input("write a name: "))

if len(userResponse) >= 7:
    print("you name must iclude less than 7 letters. ")
else:
    print(userResponse[:1] + userResponse[2] + userResponse[-1:])