
'''
The Accumulator class is very simple. It saves a tally of numbers.
The __init__ method initializes the class with a starting count of zero.
Internally, the tally is saved in the self._count variable.
This variable should be treated as private because it is prefixed with a single underscore.
The count method returns the value of the count.
This method is a property, as denoted by the @property decorator.
In Python, properties control how callers can "get" and "set" values.
With this property, a caller can get the value of count but cannot set the value directly with an assignment statement.
Finally, the add method is the only way to change the internal count value.
It accepts an amount to add as input and adds this amount to the internal account.
By default, the amount to add is one, but this value may be overwritten.
'''


class Accumulator:
    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more