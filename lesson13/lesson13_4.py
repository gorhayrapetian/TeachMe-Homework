# Random Lottery Pick. Generate 100 random lottery tickets and pick
# two lucky tickets from it as a winner.
# Note you must adhere to the following conditions:
# ● The lottery number must be 10 digits long.
# ● All 100 ticket number must be unique.

import random

ll = []

for i in range(100):
    ll.append(random.randrange(1000000000, 9999999999))

w = random.sample(ll, 3)

print('the winner is ', w[0])
print('the winner is ', w[1])
print('the winner is ', w[2])