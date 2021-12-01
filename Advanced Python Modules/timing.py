"""
Timing your code
Sometimes it's important to know how long your code is taking to run, 
or at least know if a particular line of code is slowing down your entire project. 

Python has a built-in timing module to do this.
"""

def func_one(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return [str(num) for num in range(n)]

def func_two(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return list(map(str,range(n)))

func_one(10)
func_two(10)

"""
Timing - simple method
"""
import time

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_one(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time
print(end_time)

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_two(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time
print(end_time)


"""
Timeit module - standard way
"""
import timeit

stmt1 = 'func_one(100)'
setup1 = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
timeit.timeit(stmt1, setup1, number=10000)

stmt2 = 'func_two(100)'
setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
timeit.timeit(stmt2, setup2, number=10000)


"""
Timing you code with Jupyter "magic" method
"""
'''
%%timeit
func_one(100)

%%timeit
func_two(100)
'''