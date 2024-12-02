# class : blueprint or template of an object 
# object : instance of a class 
# self : first parameter of a class which is defined inside the functions --->> keyword in python 
# function inside the class is called as methods !!

#NOTE : class name is always in capital letters !! the code will run, no error will be shown but it is the standard way to define the class

class Person:
    def hello(self):
        print("this is my hello method")
    def show(self):
        print("This is my show")

obj=Person()
obj.hello()

obj1=Person()
obj1.show()

#we can define the empty class also using the pass keyword !!
# class A:
#     pass