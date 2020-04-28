fruits = ["mango", "grapes", "bannanas", "raw mango"]

for fruit in fruits:
    print("would you like to have {}?".format(fruit))


for number in range(1,11):  # not range function max limit is the limit it is not included in the range
    print("number {}".format(number))


temprature_f = 40

while temprature_f>32:
    print("water temprature is {}".format(temprature_f))
    temprature_f -= 1
if temprature_f == 32:
    print("water freezes at 32 Fahranite")


'''
Apart from given conditions how else loop can be controled 

Break
end the loop. Go to the next statement in the program i.e. outside the loop

Continue
Skip current part of the loop and continue with the next part

Pass
Skips any part of the loop where "pass" appears. best used testing code
'''