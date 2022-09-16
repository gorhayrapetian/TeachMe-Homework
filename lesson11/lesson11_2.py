# Write a function in Python to count uppercase characters in a text
# file.

def upper(name):
    ll = []
    with open(name, 'r') as file:
        for line in file:
            line = line.split()
            for word in line:
                if word[0].isupper():
                    ll.append(word)
        return ll

print(upper('story.txt'))