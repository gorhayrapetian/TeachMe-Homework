# sxala ashxatum

lowerCase = []
upperCase = []

word = 'PYThon'

for x in word:
    if x.islower():
        lowerCase.append(x)
    elif x.isupper():
        upperCase.append(x)

print(lowerCase + upperCase)
