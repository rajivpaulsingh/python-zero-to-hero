# Create a generator that generates the squares of numbers up to some number N.
def gensquare(n):

    for x in range(n):
        yield x**2

# Run
for number in gensquare(10):
    print(number)