"""
Dictionary Comprehensions
Just like List Comprehensions, Dictionary Data Types also support their own version of comprehension for quick creation. 
It is not as commonly used as List Comprehensions, but the syntax is:
"""
{x:x**2 for x in range(10)}

# Iteration over keys, values and items
d = {'k1':1, 'k2': 2}

for k in d.keys(): # also d.iterkeys()
    print(k)

for v in d.values(): # also d.itervalues()
    print(v)

for item in d.items(): # also d.iteritems()
    print(item)


# Viewing keys, values and items
key_views = d.keys()
print(key_views)

d['k3'] = 3
print(d)
print(key_views)
