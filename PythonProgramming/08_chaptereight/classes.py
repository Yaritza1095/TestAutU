'''
Python classes allow programmers to group data and information like variables and functions into a single organized unit.
Classes can be organized one to a file, or multiple classes that share similar types of functionality can be organized into the same file.
Class features
- inheritance: derived/child class can use attributes and methods of parent class
-multiple inheritance: derived/child class can inherit attributes and methods from more than one class.
-polymorphism: derived/child class can override class methods of parent class.
The statements or information inside of a class are usually functions, but a class can also contain class variables that are specific to the class and usable throughout the entire class.

There are also variables called instance variables and those variables are specific to any Objects that are created by the class.
There are some features of a class which will require more explanation including:

-The __init__ method, which allows every instance of a class to be created with specific parameters
-The self variable which allows information to be shared easily and efficiently.
'''
import random

#The init method
'''
sets attributes for an object at object creation: is a constructor**
__init__ method is not required BUT is generally used to set
default state of object when it is created
The __init__ method is the first method in a class.

**The word constructor is another word that can be used to refer to
the __init__ method

what this does is set the attribute for the object, for example, the characteristics.
If I had a class for “Person”, I might want to set the person's first name and last name and perhaps a telephone number or an address.

The __init__ method has parameters that accept arguments which determine the attributes of the Object when it is created.


Once the parameters are given, those parameters are available to every class method.

'''

#The self variable
'''
The self variable in Python represents an instance of a class, and specifically it references the instance of the class that has been created.
We use self in order to make available all of the attributes to the methods throughout the class.
However, if a method is running as a part of the class rather than as an instance of the class, then we do not need to use the self parameter in the method.
'''
#Creating a custom class in python
class Person:
    def __init__(self, firstname, lastname, health, status):
        "initialize attributes to be used in/available for all\
        class methods in this class, and for all class objects created\
        by this class."
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status
    def introduce(self):
        "All people introduce themselves"
        print("Hi, I'm {} {}".format(self.firstname, self.lastname))
    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little tired today.".format(self.firstname))
        elif self.health >=51:
            print("{} feels unwell.".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor.".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))

Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)
print("{} Is my friend? {}".format(Maria.firstname, Maria.status))
print("{} Is my friend? {}".format(Rey.firstname, Rey.status))
Maria.introduce()
Rey.introduce()
Lee.introduce()
Maria.status_change()
Rey.status_change()
Lee.status_change()