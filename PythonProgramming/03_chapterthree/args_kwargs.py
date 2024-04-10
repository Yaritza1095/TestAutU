""""
Args = Arguments.

*args= allows for unlimited variables to be passed into a function
without defining them ahead of time.

kwargs = Keyword arguments.
**kargs = allows for unlimited keyword arguments to be passed
into a function without defining them ahead of time
"""
def user_info(name, age = 0, city = "Houston"):
    ''' This function prints name, age, and city from an argument provided to the function'''
    print("{} is {} years old, from {}".format(name, age, city))

user_info("Janet", 58, "Oklahoma City")
user_info("Micah")
user_info( age = 56, name = "Kadeem")

#*args: allows a function to take any number of positional arguments.
def add(*args):
    print(sum(args))
add(2, 3, 4)
add(2, 4, 6, 8, 184)

#**kwargs: allows a function to take any number of keyword arguments.

def application(**kwargs):
    print(kwargs)
application(name = "Jess", email = "mail@mail.com")
application(name = "Susan", surname = "Johnson", agen = 42)

"""
Combining arg types:

All three argument types can be used in a single function. They must be
used in order: formal positional arguments, *args, **kwargs

"""

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))

application("Jess", "Ingrass", "mail@mail.com", "Teach code", 75000, hire_date = "September 2010")
