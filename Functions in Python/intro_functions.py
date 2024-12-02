#Non-parameterized functions 
# def fun():
#     return "Hello this is my first non parameterized function"
# print(fun())

# def fun1():
#     print("Hello this is my second non parameterized function")
# fun1()

#how to call functions --->> we can call functions using function name 

#Parameterized Functions 
# def addition(a,b):
#     return a+b 
# print(addition(4,3))

# def substraction(a,b):
#     return a-b 
# print(substraction(7,5))

# def multiplication(a,b):
#     return a*b 
# print(multiplication(3,6))

# def division(a,b):
#     return a/b 
# print(division(10,2))

# write a function to check whether the given number is even or odd
# def number(a):
#     if a%2 == 0:
#         print(a,"is Even Number") 
#     else:
#         print(a,"is Odd Number")

# number(10)
# number(15)

#write a function to find factorial of a given number 
# def factorial(num):
#     result = 1
#     total = result * num
#     num = num - 1
#     print(total,"is the factorial of a given number")
# factorial(5)

# def factorial(num):
#     fact = 1
#     while num>=1:
#         fact=fact*num 
#         num=num-1
#     return fact

# print(factorial(5))

#types of actual arguments!!
#positional arguments -->> we have to pass the arguments in the same order as the parameters are defined in the function 
# def greet(name, age):
#     print(f"Hello, {name}! You are {age} years old.")

# greet("Alice", 25)  # Positional arguments: "Alice" -> name, 25 -> age

#keyword arguments -->> we have to specify the parameter name in this type of arguments
#the order doesn't matter !! -->> only give the proper keyword name
# def meet1(name,age):
#     print(f"Hello {name}! You are {age} years old.")
# meet1(age=21,name='Shrikant')


#default arguments 
# def wish(name="Guest"):
#     print("Hello",name,"Good Morning!")
# wish("Shrikant")
# wish() #here i have not passed arguments inside the function which i have created then it will take the default parameter which i have defined at the initialization of a function 

# def addition(a=10,b):
#     print(a+b)
# addition(30,10)  #SyntaxError: parameter without a default follows parameter with a default
#it is positional error now we have to change the position 

# def addition(b,a=10):
#     print(a+b)
# addition(30)

# def substraction(b,a=15):
#     print(a-b)
# substraction(20) #o/p" -5


#if we are passing two default parameters in one funtion and at the time of calling we are passing only one parameter then second parameter will be consider as the last default parameters 

#variable length arguments -->> used when we don't know how many arguments user will be going to insert 
def sum (*n):
    total = 0
    for n1 in n:
        total = total + n1
    print("The Sum=",total)

#sum(4,5,6,7)
sum(10,20,30)       