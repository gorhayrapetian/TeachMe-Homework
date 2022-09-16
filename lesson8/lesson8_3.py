# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.

num = int(input('Enter a number: '))

def func(x):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
        print(factorial)
    return x

func(num)