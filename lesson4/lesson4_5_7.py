
# The program prompts the user their birth year. Assuming a person’s age
# is a non-negative integer not exceeding 120, output the user’s age or the
# words “Incorrect Year”. The sample outputs assume it’s currently the year
# 2016. If you are writing this program during any other year, the correct
# answers may differ. Store the value of the current year in a variable.

user_response = input('when did you born?: ')

age = 2022 - int(user_response)

if int(user_response) < 0:
    print('incorrect year. ')
elif int(user_response) > 2022:
    print("you can't be born in the future. ")
elif int(age) > 120:
    print('you have to be younger than 120 y.o. ')
else:
    print('you are ' + str(age) + ' years old')