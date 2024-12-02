#special method in python used to destroy objects 
#used for cleanup activity 
#defined by "del" keyword 
# a=10
# print(a)
# del a 

# print (a)
class Disc():
    def __init__(self,name):
        self.name=name
 #now a is deleted from the memory now it will show the error as --->> NameError: name 'a' is not defined

    print("Shrikant calling constructor")

    def display(self):
        return self.name
    
    def __del__(self):  #we can define the destructor using "__del__" keyword!!
        print("Calling destructor")
    
obj=Disc("Sakshi")
print(obj.display())
del obj  #deleting the object that i have created!! 

print(obj.display()) #after deleting the object or after callling the destructor this line will won't be printed!! --> shows the error as : NameError: name 'obj' is not defined