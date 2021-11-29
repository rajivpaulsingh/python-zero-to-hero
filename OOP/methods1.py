class Circle:

    #  CLASS LEVEL ATTRIBUTE
    pi = 3.14

    # Circle gets instanciated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius
        self.area = Circle.pi * radius * radius

    # METHOD
    def get_circumference(self):
        return 2 * self.pi * self.radius

my_circle = Circle(30)

# Runnable
print('Radius is:', my_circle.pi)
print('Area is:', my_circle.area)
print('Circumference is:', my_circle.get_circumference())
