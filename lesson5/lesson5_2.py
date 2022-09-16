# Write a Python program to get the largest number from a list.

li = []

for i in range(5):
    num = int(input("Write the another number: "))
    li.append(num)
li.sort()

print("This is the largest number of the list:", li[-1])