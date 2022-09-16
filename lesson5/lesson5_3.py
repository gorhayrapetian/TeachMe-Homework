# Write a Python program to get the smallest number from a list.

numbers = []


for i in range(5):
    num = int(input("Write the another number: "))
    numbers.append(num)
numbers.sort()

print("This is the smallest number of the list:", numbers[0])