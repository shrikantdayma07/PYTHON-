#it is an unexpected event that disrupt the flow or execution of the program!!
# there are two types of  error :
# 1] syntax error --->> error occurs due to programmer mistake!!
# 2] run-time error --->> also known as exceptions !! 
#programmer is responsible to correct these syntax errors. 

#syntax : 
'''try:
    #risky code 
except:
    #handle exception
    #executed when exception occured in try block 
else:
        will be executed if there is no exception inside the try block
finally:
        will be executed whether exception raised or not raised and handled or not '''


#exceptional handling concept applicable for run-time error not for syntax error !!
# a=int(input("enter the value of a: "))
# b=int(input("enter the value of b: "))
# print(a/b) #if i enter value of b as 0 then it will give error as ---->> ZeroDivisionError: division by zero

# a=int(input("Enter the value of a: "))
# b=(input("Enter the value of b: ")) # as there is not datatype mentioned then it will give typeError 
# #TypeError: unsupported operand type(s) for /: 'int' and 'str'
# print(a/b)

#example of exceptional handling using try and except block
# a=int(input("enter the value of a: "))
# b=int(input("enter the value of b: "))
# try:
#     print(a/b)

# except:
#     print("do not enter value as zero")

# try:
#     a=input("enter the value of a: ")
#     b=input("enter the value of b: ")
#     print(int(a)/int(b))
# except ZeroDivisionError:
#     print("Sorry we can't divide a number by zero")
# except TypeError:
#     print("Type Error")
# except ValueError:
#     print("Please enter numbers only")


#finally : this will always be executed whether there will be exception or not in the code 
#finally block executes whenever there is error or not!!
try:
    a=input("enter the value of a: ")
    b=input("enter the value of b: ")
    print(int(a)/int(b))
except ZeroDivisionError:
    print("Sorry we can't divide a number by zero")
except TypeError:
    print("Type Error")
except ValueError:
    print("Please enter numbers only")
else:
    print("no exception in the try block") #it will execute if there is no exception in the try block and if there is exception then no else block will be executed 
finally:
    print("Its finally!!") #it will execute in both time whenever there is error or not!!