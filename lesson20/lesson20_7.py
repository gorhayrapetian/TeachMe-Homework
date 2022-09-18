# Dict comprehension value same as key (numbers = [1,2,3,4,9,47] )
# ○ Output {1:1, 2:2, 3:3, :4:4, 9:9, 47:47}

numbers = [1, 2, 3, 4, 5]

dict1 = {x: x for x in numbers}

print(dict1)