def add():
    a = float(input("Enter a number."))
    b = float(input("Enter another number"))
    print (a+b)

def substract():
    a = float(input("Enter a number."))
    b = float(input("Enter another number"))
    if a > b:
        print(a-b)
    else:
        print(b-a)

def mulitply():
    a = float(input("Enter a number."))
    b = float(input("Enter another number"))
    print(a*b)

def divide():
    a = float(input("Enter a number."))
    b = float(input("Enter another number"))
    print(a / b)

operation = input("Please type operation you want to perform  + OR  - OR  * OR /" )
if operation == "+":
    add()
elif operation == "*":
    mulitply()
elif operation == "-":
    substract()
elif operation == "/":
    divide()
else:
    print("Please enter correct operation")

