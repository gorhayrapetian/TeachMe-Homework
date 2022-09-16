# Get the same items in two ranges using nested loop, (0,10),(5,15)

for x in range(0,10):
    for y in range(5,15):
        while x == y:
            print(x)
            break
