# Create cubes of numbers and storing it in list
def create_cubes1(n):

    result = []
    for x in range(n):
        result.append(x**3)

    return result

# Run 1
print(create_cubes1(10))
# Run 2
for x in create_cubes1(10):
    print(x)



# Create cubes of numbers using yeild wihout storing in list
def create_cubes2(n):

    for x in range(n):
        yield x**3

# Run
for x in create_cubes2(10):
    print(x)