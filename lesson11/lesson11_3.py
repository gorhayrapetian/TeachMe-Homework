# Write a Python function to read first n lines of a file.

n = int(input('Enter a number: '))

with open('story.txt', 'r') as file:
    for i in range(n):
        print(file.readline())