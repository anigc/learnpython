def user_info(name, age, city):
    '''
    This function prints the name, age, city provided as input
    :param name:
    :param age:
    :param city:
    :return:
    '''

    print("{} is {} years old, from {}".format(name, age, city))

#user_info("Ani", 66, "PLanet Earth")

#Above part shows how arguments can be paseed to a function

#Now we will see how arguments are treated as positional arguments

#user_info("Jessica", "Mumbai")
'''
#For the above call it throws error saying
 "user_info() missing 1 required positional argument: 'city'
 However call gives Name and CIty but age is missing
 
 the error and the argument comparision shows that python treats the argument based on position
 i.e. argument at postiion 1 is name, position 2 is age and position 3 is city
 
 THis can  be overcome by keyword argument
 
'''
'''
Keyword argument
1. Set defaults i.e. what value taken if the argument is not provided
i.e age=0, city="not provided"
'''

def user_info2(name, age=0, city="city not provided"):
    print("{} is {} years old, from {}".format(name, age, city))


user_info2("Namita")
#user_info2(age=56, name="Rohit")

'''
*args = providing n number of positional arguments
**kwargs = providing n number of keyword arguments

Combiing the argument type
formal positional arguments, args and kwargs can be comboined in the order
postiional argument, *args, **kwargs
'''


def user_info3(fname, lname, age, company, email, *args, **kwargs):
    print("{} {} is {} years old, works in {} with email id {}".format(fname, lname, age, company, email))


user_info3("Rahul", "Sharma", 22, "Tech.org", "test@test.com", 75000, hire_date = "15-Sep -2019")


def user_info4(fname, lname, age, company, email, *args, **kwargs):
    print("{} {} is {} years old, works in {} with email id {}".format(fname, lname, age, company, email))


user_info4("Rahul", "Sharma", 22, "Tech.org", "test@test.com", 75000, hire_date = "15-Sep -2019")






