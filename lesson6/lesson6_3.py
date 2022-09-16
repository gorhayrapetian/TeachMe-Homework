# Count all letters, digits, and special symbols from a given string

word = input("Please Enter your Own String : ")

letters = digits = symbols = 0

for i in range(len(word)):
    if word[i].isalpha():
        letters = letters + 1
    elif word[i].isdigit():
        digits = digits + 1
    else:
        symbols = symbols + 1

print('letters: ' + str(letters))
print('digits: ' + str(digits))
print('symbols: ' + str(symbols))