# Generate a random Password which meets the following conditions
# ● Password length must be 10 characters long.
# ● It must contain at least 2 upper case letters, 1 digit, and 1 special
# symbol.

# sxal em arel bayc im miak dzevn er 

import random

simbols = '~!@#$%^&*|?/._-'

numbers = '0123456789'

letters = 'abcdefghijklmnopqrstuvwsxyz'

uppLetters = 'ABCDEFGHIJKLMNOPQRSTUVWSXYZ'

a = random.choice(simbols)

b = random.choice(numbers)

c = random.choice(letters)

d = random.choice(uppLetters)

password = []

p = (a + b + c + d)

for i in p:
    password.append(i)

random.shuffle(password)

print(''.join(password))

