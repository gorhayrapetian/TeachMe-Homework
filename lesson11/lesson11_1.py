# Write a Python function to count the number of lines from a text file
# "story.txt" which is not starting with a letter "T"

def func(name):
    with open(name, 'r') as file:
        count = 0
        for line in file:
            if line[0] != 'T':
                count += 1
        return count

print(func('story.txt'))