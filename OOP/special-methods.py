"""
Finally let's go over special methods. 

Classes in Python can implement certain operations with special method names. 
These methods are not actually called directly but by Python specific language syntax. 

For example let's create a Book class:
"""

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    # SPECIAL METHOD
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is deleted")


mybook = Book("Python Rocks!", "Jose Portilla", 159)

# Special Methods
print(mybook)
print(len(mybook))
del mybook