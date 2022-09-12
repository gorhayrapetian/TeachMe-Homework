# Input two positive integers, and output a line describing their relation.
# Follow the sample format.

user_response = input('write a number: ')
user_response_2 = input('write your second number: ')

if user_response > user_response_2:
    print(user_response + ' > ' + user_response_2)
elif user_response < user_response_2:
    print(user_response + ' < ' + user_response_2)
elif user_response == user_response_2:
    print(user_response + ' = ' + user_response_2)