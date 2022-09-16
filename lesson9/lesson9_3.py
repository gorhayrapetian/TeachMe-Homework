# Write python function which return whether given number is prime or
# not.

userResponse = int(input('Enter a number: '))

def function(x):
    if x == '2':
        print(x, 'is prime')
        return x
    elif x % 2 == 0 and x <= 1:
        print(x, 'is not prime')
        return x
    for i in range(2,9):
        if x % i == 0:
            print(x, 'is not prime')
        else:
            print(x, 'is prime')
        return x


function(userResponse)
