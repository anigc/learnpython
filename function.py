def addition():
    a = 11.23
    b= 30
    print(a + b)

addition()

#taking user input using input() function
"""
here input is the name of the built in python function
() has the user prompt i.e. to give question or direction to the user
the prompt is always a string and input this prompt takes is also a string
As it takes in only string using the function int to convert the string input into an integer
"""

def addition2():
    a = int(input("enter a number. "))
    b= int(input("enter another number. "))
    print(a + b)


addition2()