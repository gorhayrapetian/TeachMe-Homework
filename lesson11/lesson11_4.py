# Write a Python function to write a list to a file

ll = ['another line', 'another line 2', 'another line 3']

with open('story.txt', 'a') as file:
    print(file.write(ll[0]))