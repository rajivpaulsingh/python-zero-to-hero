class Dog:

    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANT INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self, breed, name, spots):

        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots

    # OPERATIONS/Actions --> Methods
    def bark(self):
        print('Woof woof!, my name is {}'.format(self.name))

my_dog = Dog(breed='Lab', name='Jacky', spots=True)

# Runnable
print(type(my_dog))
print(my_dog.species)
print(my_dog.name)
my_dog.bark()