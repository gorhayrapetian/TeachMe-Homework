# Given dictionary is consisted of vehicles and their weights in kilograms. Construct a list
# of the names of vehicles with weight below 5000 kilograms. In the same list
# comprehension make the key names all upper case.

dict1 = {'truck': 2500, 'airplane': 30000, 'car': 1500, 'ship': 45000}

dict2 = {k.upper(): v for (k, v) in dict1.items() if v < 5000}

print(dict2)