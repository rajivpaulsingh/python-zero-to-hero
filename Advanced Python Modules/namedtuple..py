# A namedtuple assigns names, as well as the numerical index, to each member.

# Simple tuple
t = (12, 13, 14)
t[0] # this will give 12

# Named tuple
from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
jack = Dog(age=2, breed='Lab', name='Jakie')
frank = Dog(age=3, breed='Huskie', name='Frankie')

# Run
print(jack)
print(jack.age)
print(frank.breed)