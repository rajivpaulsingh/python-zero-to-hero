class Dog:
    def __init__(self, breed, name, spots):

        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed='Huskie', name='Sam', spots=False)

# Runnable
my_dog.breed
my_dog.name
my_dog.spots