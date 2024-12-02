#import statement 

#syntax 1 : import module_name 

'''where import is keyword used to import module '''

#syntax 2 : from module_name import variable, function, class 

#according to syntax 1
# import mymodule
# print(mymodule.x)

#according to syntax 2
# from mymodule import x,y
# print(y)

# from random import *
# print(random())

#randrange([start],stop,[end]): 
# from random import * 
# print(randint(1111,9999))
# for i in range(10):
#     print(randrange(10))

#random() : this function generate some float value between 0 and 1 (not inclusive)
# from random import *
# print(random()) #o/p : 0.9488951033368587

#randint() : to generate random integer between two given numbers(inclusive)
# print(randint(1111,9999)) #o/p: 6590

#uniform() : it return random float value between 2 given numbers 
# from random import *
# print(uniform(100,999)) #o/p : 271.46721893134406

#randrange(): returns a random number from the range 
from random import * 
print(randrange(10)) #o/p: 3
# print(randrange(1,11)) #o/p : 5
print(randrange(0,11,2))  #o/p : 2

#choice() function
'''it won't return random number
it will return a random object from the given list or tuple'''

import random
names=['shrikant','anuj','krishna','jay','shubham','samir','chirayush','naitik']
print(random.choice(names))


#package() : any folder or directory consists of __init__.py file 
#but basically this init.py file is nothing but a package which is empty !!
# folder in linux is called as directory!!