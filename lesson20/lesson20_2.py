# Find the common numbers in two lists (without using a tuple or set) list_a = [1, 2, 3, 4],
# list_b = [2, 3, 4, 5]

list_a = [1, 2, 3, 4]

list_b = [2, 3, 4, 5]

list_c = [x for x in list_a if x in list_b]

print(list_c)