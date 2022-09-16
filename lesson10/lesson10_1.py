# Write a Python program to square and cube every number in a given list of
# integers using Lambda.

x = (1, 2, 3, 4, 5)

result = map(lambda x: x ** 2, x)
result2 = map(lambda x: x ** 3, x)

print(list(result), list(result2))