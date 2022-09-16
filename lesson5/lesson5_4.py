# Write a Python program to find the second smallest number in a list.

numbers = []

for i in range(5):
    num = int(input("Enter the another number: "))
    numbers.append(num)
numbers.sort()

print("The second smallest value of this list: ", numbers[1])