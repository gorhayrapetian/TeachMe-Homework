# Write a Python program to remove duplicates from a list.

li = []

for i in range(5):
    num = int(input("Write a number: "))
    li.append(num)
li.sort()

print("This is the list without duplicates: ", set(li))