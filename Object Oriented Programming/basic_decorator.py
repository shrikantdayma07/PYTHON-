#decorator : takes parameter as a function and return  function as output 
class B:
    course = "Full stack" #class variable- declare inside the class  

    def __init__(self,name):
        self.name=name  #instance variable  --->> the variable which is initialized under the constructor are called as instance variable 

    @classmethod    #this is called as decorator 
    def display(cls):   #class name in the decorator is named as "cls"
       return cls.course #NameError : name 'course' is not defined 

print(B.display()) #need not to create object in the class method in the decorator !! 