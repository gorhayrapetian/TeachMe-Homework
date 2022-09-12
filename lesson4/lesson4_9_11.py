# Given a real number, round it to the nearest whole.

num = input('write a number: ')

if int(num[2]) < 5:
    print(num[0])
elif int(num[2]) > 5:
    print(int(num[0]) + 1)