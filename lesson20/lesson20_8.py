# Flipping key value pairs in a dictionary using dict comprehension
# (a = {"a":10, "b":20, "c":30}
# ○ Output {10: ‘a’, 20: ‘b’, 30: ‘c’}

a = {"a": 10, "b": 20, "c": 30}

b = {k: v for (v, k) in a.items()}

print(b)