#there are basically two types of variables in python :- 1] local variable 2] global variable 

''' local variable is one which is created inside the functions and can be called locally whereas global variable is one which is created outside the functions and can be called inside or outside the functions as it is globally created '''

#creating the local variables 
# def local_variable():
#     s="Shrikant Dayma"
#     print(s)

# local_variable()

#creating the global variables
# def f():
#     s='I love India'
#     print("inside function: ",s)

# f()
# print(s)  #now it will give error as name 's' is not defined

#s="Hello World!"
def f():
    s=50
    print(s)


f()
print(s) #as 's' is defined locally inside the function locally then it cannot be called outside the function --->> gives you the error!!
