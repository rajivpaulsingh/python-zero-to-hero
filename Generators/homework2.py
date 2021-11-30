# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library.

import random

random.randint(1, 10)

def rand_num(low, high, n):

    for x in range(n):
        yield random.randint(low, high)

# Run
for number in rand_num(1, 10, 12):
    print(number)