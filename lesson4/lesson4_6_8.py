# Input three integers. Output the word “Sorted” if the numbers are listed in
# a non-increasing or non-decreasing order and “Unsorted” otherwise.

user_response = input('write a number: ')

user_response_2 = input('write your second number: ')

user_response_3 = input('write you third number: ')

if user_response < user_response_2 < user_response_3:
    print('this sequence is sorted')
else:
    print('this sequence is not sorted ')