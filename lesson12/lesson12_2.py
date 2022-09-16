# Write a python program to catch error and print “Error is caught”
# You need to do it with 5 different Error

x = 5
y = 'jwnf'

try:
    result = x / y
    print(result)
except TypeError:
    print('Error is caught')
try:
    result = x / int(y)
    print(result)
except ValueError:
    print('Error is caught')
try:
    result = z / x
    print(result)
except NameError:
    print('Error is caught')