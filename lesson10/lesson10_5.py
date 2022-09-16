# Write a Python program to add two given lists using map and
# lambda.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

sum = map(lambda i, g: i + g, list1, list2)

print(list(sum)) 