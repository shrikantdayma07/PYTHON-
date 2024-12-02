#constructor :used to initialize instance variable of the class 
#special method in python 
#we can define constructor using __init__ method()
#there are three types of constructor :
# 1] default 
# 2] parameterized 
# 3] non-parameterized 

#constructor get automatically called at the time of object creation !!
# class Person:
#     def __init__(self):
#         print("calling constructor")
#     def show(self):
#         print("calling show")
    
# obj = Person() #o/p: calling constructor 

#types of constructor 
# default constructor ---->> (self) is the default constructor which is always used as a parameter 
# parameterized constructor 
# non-parameterized constructor 

#1]Parameterized constructor -->> whenever we are passing the parameters inside the function then we have to initialize the variables also !!
# class A:
#     def __init__(self,name,age):
#         self.name=name  #instance variable  --->> the variable which is initialized under the constructor are called as instance variable 
#         self.age=age    #instance variable 
#         print("Calling constructor",self.name,self.age)
# obj=A("Shrikant",21)

# Whenever we defined a method inside a class with self as a keyword or parameter is called instance method 
# class A:
#     course = "Full stack" #class variable- declare inside the class  

#     def __init__(self,name,age):
#         self.name=name  #instance variable  --->> the variable which is initialized under the constructor are called as instance variable 
#         self.age=age    #instance variable 
#         print("Calling constructor",self.name,self.age)

#     def show(self):      #we have to pass "self" as an argument compulsory else it will give the error as -->> " TypeError: A.show() takes 0 positional arguments but 1 was given "
#         print(self.name,self.age,self.course)

#     def display(self):
#         print(course) #NameError : name 'course' is not defined 

# obj=A("Shrikant",21)

# obj.show()

# print(obj.name)   #we can print the instance variable outside the object also !!

# print(A.course) #class variable is called!!

# print(A.display())   #shows errror 

#decorator : takes parameter as a function and return  function as output 
class A:
    course = "Full stack" #class variable- declare inside the class  

    def __init__(self,name,age):
        self.name=name  #instance variable  --->> the variable which is initialized under the constructor are called as instance variable 
        self.age=age    #instance variable 
        print("Calling constructor",self.name,self.age)

    def show(self):      #we have to pass "self" as an argument compulsory else it will give the error as -->> " TypeError: A.show() takes 0 positional arguments but 1 was given "
        print(self.name,self.age,self.course)

    @classmethod    #this is called as decorator 
    def display(cls):   #class name in the decorator is named as "cls"
        print("Course name is: ",cls.course) #NameError : name 'course' is not defined 

obj=A("Shrikant",21)

obj.show()

print(obj.name)   #we can print the instance variable outside the object also !!

print(A.course) #class variable is called!!

print(A.display())

# print(obj.display()) #gives the same o/p as A.display() !! 
