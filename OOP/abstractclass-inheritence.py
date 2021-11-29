"""
A more common practice is to use abstract classes and inheritance. 
An abstract class is one that never expects to be instantiated. 

For example, we will never have an Animal object, only Dog and Cat objects, 
although Dogs and Cats are derived from Animals:
"""

class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def speak(self):   # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        print(self.name + " says Woof!")

class Cat(Animal):
    def speak(self):
        print(self.name + " says Meow!")

mydog = Dog('Tommy')
mycat = Cat('Kitty')

mydog.speak()
mycat.speak()