try:
    f = open('testfile', 'r') # Only read permissions
    #f = open('testfile', 'w')
    f.write('Test write this')
except TypeError:
    print('There was a type error')
except OSError:
    print('Hey you have an OS error')
finally:
    print('I always run')