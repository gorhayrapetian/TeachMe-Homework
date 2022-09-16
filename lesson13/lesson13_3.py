# Generate a random date between given start and end dates

import random 
import datetime

date = datetime.date(random.randint(2005,2025), random.randint(1,12), random.randint(1,31)) 
print(date) 