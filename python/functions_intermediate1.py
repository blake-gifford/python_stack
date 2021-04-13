

# 1. write a function that takes 2 arguments
# 2.if no arguments will return random number 0-100
# 3.if only 1 max num provided return random num 0-max num
# 4.only min num provided should return random num min-100
# 5.both min and max provided return random between



import random
def randInt(min=num, max=num):
    num = random.random() 
    return num
    if min==" " & max=="":
        min=0 
        max=100
    elif min=="" & max==12:
        min=0
    elif min==0 & max=="":
        max=100
    else min=0 & max=100:
randInt(num,num)
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

