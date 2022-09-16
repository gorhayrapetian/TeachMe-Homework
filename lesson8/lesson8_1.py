# Write a Python function to find the Max of three numbers.

ll = [5, 11, 3]

def maximum(ll):
    ll.sort()
    return ll[-1]

print(maximum(ll))