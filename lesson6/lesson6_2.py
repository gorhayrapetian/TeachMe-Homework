lowerCase = []
upperCase = []

word = 'PYThon'

for x in word:
    if x.islower():
        lowerCase.append(x)
    elif x.isupper():
        upperCase.append(x)

word = lowerCase + upperCase

print(''.join(list))
