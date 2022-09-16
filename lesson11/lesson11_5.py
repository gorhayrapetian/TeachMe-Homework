# Write a function in Python to count words in a text file those are
# ending with letter "e"

def count_e(name):
    count = 0
    with open(name, 'r') as file:
        for line in file:
            line = line.split()
            for word in line:
                if word[-1] == 'e':
                    count += 1
        return count

print(count_e('story.txt'))