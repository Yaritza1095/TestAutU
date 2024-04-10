'''
Multiple Inheritance
Multiple inheritance is when one class inherits from multiple classes and is able to use attributes and methods from both classes.
There are pros and cons to using multiple inheritance.

Pros include the ability to reuse small amounts of code in multiple classes and mix-ins.
Cons include the order of inheritance matters. Inheriting from multiple classes can become quite complicated depending on the number of classes, the names of class methods and other factors, including common attributes shared among multiple parent classes.

There can be more maintenance involved when refactoring code that is using multiple inheritance.
Typically, if we have multiple classes that we want to inherit from, we'll have the attributes of each class and then bring in the attributes of the class individually into the initialization or __init__ method of the child class.
'''
class Item:
    def __init__(self, sku):
        self.sku = sku
    def print_sku(self):
        print("The sku is {}".format(self.sku))
class Garment:
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.type))

#child class
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.name))

Blouse = Shirts("00001", 42, "Tops", "Formal Blouse", "White")
Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()

