#class example
class Person:
    def __init__(self, firstname, lastname, health, status):
        " initialize attributes to be used in/available for all \
        class methods in this class, and for class objects created \
        by this class."

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >=76:
            print("{} is a little tired today.".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))

Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()

'''
Inheritance
Inheritance is when we use the attributes and methods from the parent class 
and make those attributes and methods available to the child's class.
In order to access all of those attributes, we use the super method.

In the super method, all of the attributes of the parent class are accessed. 
Then we can set any new attributes in the child's class.
'''

#inheritance example
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon
    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -=5
        print(other.health)
    def insult(self, other):
        if other.health <80:
            print("{} you are tired and weak.".format(other.firstname))
    def steal(self, other):
        print("ha, ha, ha {}, I have your stuff!".format(other.firstname))

        if other.status == True:
            other.status = False

    '''
    Polymorphism — Method Overriding

    Polymorphism occurs when we want to allow the child class to have a method with the same name and a similar implementation as the parent class and we wish for that method 
    you override the parent class method.
    '''
    def introduce(self):
        print("You are my mortal enemy!")


Alex = Enemy('rock', 'Alex', 'Wayne', 75, status=False)
Alex.hurt(Maria)
Alex.insult(Lee)
Alex.steal(Rey)
Maria.introduce()
Rey.introduce()
Alex.introduce()




