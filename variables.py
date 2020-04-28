# to create a comment in python use #
# variable naming conventions : lower case/upper case, numbers or can start with _
# variables are case sensitive. CARS and car are different
#for multiname variable use underscores

_cars = 23

CASRS = 24

cars = 25

number_of_cars = 4

kind_of_cars = "Ferrari"

print(_cars)
print(cars)
print(CASRS)
print(number_of_cars)
print(kind_of_cars)

# what happpens if one uses same variable twicein a row
# it uses the latest value as below

cars_twice = 33
cars_twice = 34
print(cars_twice)

#Data type

#String : Strings are enclosed in double quotes or single quotes
#       : are immutable

#Integers: Whole numbers : Mathematical operations can be performed

#Fractional numbers: Mathematical operations can be performed
#: Python has ability to find and count the number of decimal places

"""
THis format is for the multiline comment 
"""

"""
String formatting
"""
name = "Anita Gujrathi"
school = "N I Highschool"
print (name+school)
print (name + " " + school)
print(name + "studied at" + school + ".")

#using string format method
print("{} studied at {}".format(name, school))