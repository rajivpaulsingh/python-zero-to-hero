class Animal:

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("Nom nom nom!")

# Inheriting the base class (Animal)
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    # Override
    def who_am_i(self):
        print("I am a dog")

    # Add new method
    def bark(self):
        print("Woof!")    

mydog = Dog()
mydog.who_am_i()
mydog.eat()
mydog.bark()