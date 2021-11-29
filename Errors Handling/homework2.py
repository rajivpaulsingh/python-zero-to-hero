"""
Handle the exception thrown by the code below by using try and except blocks. 
Then use a finally block to print 'All Done.'
"""

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by Zero")
finally:
    print("All Done")