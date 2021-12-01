import random

print(random.randint(0, 100)) # It will give different number everytime

# To use the same random number evertime, we use seed (it has to be in the same cell in jupyter)
random.seed(101)
print(random.randint(0, 100))


# Grab a random item from a list
mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist)) # choose random number

# Shuffle a list
random.shuffle(mylist)
print(mylist)