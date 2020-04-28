'''
What is list?
collection of data
can contain any/all data types in a single list
can contain other collections (list, directories, tuples) as list item
mutable (items can be added removed changed)
maintain order (can use index to find item)
'''

fruits = ["grapes", "mango", "muskmelon"]

years = [3, "1998", 2.5, 987, "1994"]

print(fruits, years)

#append
fruits.append("lemon")

# extend: to add/append more than one item to the list i.e. adding list to a list
fruits.extend(years)
print(fruits)

fruits.pop(0)
print(fruits)

fruits.pop(-1)
print(fruits)

numbers = [5, 1928, 4, 17, 68, 73.76]
numbers.sort();

fruits.remove("lemon")
print(fruits)

#contains
print("lemon" in fruits)
print("mango" in fruits)
