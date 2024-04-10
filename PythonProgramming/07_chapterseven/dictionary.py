'''
07_chapterseven
contents: key/value pairs
mutable: can be changed
order: maintain order of entry as of python 3.8
syntax: curly brackets contain keys and values.
Keys and values are separated by a colon.
You can make empty dictionaries by assigning a dictionary name
with nothing in the curly braces.

Example:
years = {"Layla":1974, "Ackeeem": 1997}

In this example the first key is Layla and second key is Ackeem.
Those keys are unique, they are Strings, and in this instance they are names.

The value for each of those key is a year.
For Layla is 1974 and for Ackeem is 1997.
'''

#Dictionary methods: get

stuff = {"food": 15, "energy": 100, "enemies":3}
print(stuff.get("food"))

#Dictionary methods: items
print(stuff.items())

#Dictionary methods: keys
print(stuff.keys())

#Dictionary methods: popitem (removes last item in a dictionary)
print(stuff.popitem())
print(stuff)

#Dictionary methods: setdefault: allows to set a default key value when a key is not in the dictionary and to add it to that dictionary
print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 123))
print(stuff)

#Dictionary methods: update

new_items = {"rocks": 2, "arrows": 18}
stuff.update(new_items)
print(stuff)
up_new = {"food": 3, "webs":2}
stuff.update(up_new)
print(stuff)
'''
We can update existing items in the dictionary through the same process.
So, for example, if I want to update the “rocks” and “arrows”, 
one way that I can do it is to change those right in the “new_items” dictionary.
Now, I can call the update method in the same way I did before.
'''
stuff.update(food = 450, cookies =6)
print(stuff)