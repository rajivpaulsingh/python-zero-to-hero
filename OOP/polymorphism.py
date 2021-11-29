class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says meow!"

mydog = Dog("Taiger")
mycat = Cat("Kittycat")

print(mydog.speak())
print(mycat.speak())

# One way to demonstrate polymorphism
print("One way to show polymorphism")
print("*****************************")
for pet in [mydog, mycat]:

    print(type(pet))
    print(pet.speak())

# Another way to demonstrate polymorphism is using functions
print("Another way to show polymorphism")
print("*********************************")
def pet_speak(pet):
    print(pet.speak())

pet_speak(mydog)
pet_speak(mycat)