'''
Lists

-Collection of data
-Can contain any/all data types in a single list
-Can contain other collections (lists, dictionaries, tuples) as list items
-mutable (items can be added, removed, changed)
-maintain order (can use index to find an item)
'''
'''
#List methods
fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]
print(fruits, years)

#List method: append
fruits.append("oranges")
print(fruits)

#List method: Extend
fruits.extend(years)
print(fruits)

#List method: Remove

fruits.remove("oranges")
print(fruits)

#Lis method: Pop
fruits.pop(0)
print(fruits)
fruits.pop(-1)
print(fruits)

#List method: Sort
numbers = [5, 1928, 4, 17, 68, 73.76, 20.458]
numbers.sort()
print(numbers)
'''

#Checking membership in a list
fruits = ["peaches", "apples", "pears", "apples", "apples"]
years = [3, "1998", 2.5, 987, "1994"]
print("apple" in fruits)
print("apples" in fruits)
print(fruits.count("apples"))
print(fruits.index("apples"))