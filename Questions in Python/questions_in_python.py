#this are some questions asked most frequently 

#write a program to print the following pattern 
''' *
    **
    ***
    ****
    ***** '''
        
# for i in range(6):
#     for j in range(i):
#         print("*",end="")
#     print()

# what is the difference between break and continue statement with example 

#break statement : 
#this program will exit the loop as soon as the value is 7
# for i in range(10):
#     if i == 7:
#         print("processing is enough..plz break")
#         break
#     print(i)

#continue statement 
#as soon as the number is even it will skip the number and print the next number i.e. odd numbers only /-
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

#Declare single variable of each datatype in a python. Mention function by which can find datatype of it 
# var=10
# print(type(var))

# var1=12.50
# print(type(var1))

# var2= "Hello Shrikant"
# print(type(var2))

# var3= True
# print(type(var3))

# list = [1,2,3]
# print(type(list))

# tuple = (1,2,3)
# print(type(tuple))

# set = {1,2,3}
# print(type(set))

# dict = {"name":"Shrikant"}
# print(type(dict))

#difference between list and tuple
#list : it is mutable i.e. can be modified, defined with square brackets[] allowing adding, removing and changing elements 
# list = [1,2,3]
# print(list)
# list[0]=10
# print(list) #[10, 2, 3]

#tuple : it is immutable i.e. cannot be modified after creation, defined with parenthesis(), typically used for fixed data that shouldn't change 
# tuple = (1,2,3)
# print(tuple)
# tuple[0]=5
# print(tuple) #it will give the error i.e. not allowed or not support --->> TypeError: 'tuple' object does not support item assignment

#write a program for swaping of 2 variables 
#there are 2 different logics 
# a=10
# b=20
# print("a,b= ",b,a)

# a=5
# b=15
# a=a+b
# b=a-b
# a=a-b 
# print("values of a and b are: ",a,b)

#write a program to print all the even numbers between 1 to 10
# for n in range(1,11):
#     if n % 2 == 0:
#         print(n)

#write a program to print the fibonacci series --->> 0 1 1 2 3 5 8 13 21 34 55 89 144

#initialize first two terms of the series 
# a,b=0,1
# while a<=144:
#     print(a,end=" ")
#     a,b = b, a+b 

#write a program for accepting n from the user ,and find its factorial 
# a=int(input("Enter an integer number: "))
# fact=1
# while a>=1:
#     fact = fact * a 
#     a=a-1
# print(fact)

#another logic for factorial of a number 
# Accept input from the user
# n = int(input("Enter a number: "))

# Initialize factorial to 1
# factorial = 1

# Calculate factorial using a loop
# if n < 0:
#     print("Factorial is not defined for negative numbers.")
# elif n == 0 or n == 1:
#     print("The factorial of", n, "is 1")
# else:
#     for i in range(1, n + 1):
#         factorial *= i
#     print("The factorial of", n, "is", factorial)


#write a program to check whether a number is prime or not -->> take input from the user 
# num=int(input("Enter an integer number: "))
# if num < 2:
#     print(num,"is not a prime number")
# else:
#     #assume that the number is prime 
#     is_prime = True
#     for i in range(2,num):
#         if num % 2 == 0:
#             is_prime=False
#             break
        
#     if is_prime:
#         print(num,"is a prime number.")
#     else:
#         print(num,"is not a prime number")

#write a program for accepting string from the user then find out the length of the string with and wothout len() function
#using the len() functions 
# user=input("Enter the string: ")
# length_string = len(user)
# print("Length of the string: ",length_string)

#without using the len() functions 
user=input("Enter the string: ")
len_without_str = 0
for char in user:
    len_without_str += 1
print("Length of the string without len() function: ",len_without_str)