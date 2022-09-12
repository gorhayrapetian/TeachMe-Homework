# Input a two-digit natural number and output the sum of its digits. You can
# assume that the input will be a two-digit number and need not check that
# programmatically.

user_response = input('write a number which must have at least two digits: ')

if len(user_response) < 3:
    print('your number must include at least two digits: ')
else:
    print(int(user_response[0]) + int(user_response[-1]))
